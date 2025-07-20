import re
import shutil
import subprocess

from Xlib import display

from lib.diskinfo import Disks
from lib.dmidecode import run_dmidecode, get_manufacturer, get_model, get_serial_number, get_cpu_info, get_memory
from lib.readfile import ReadFile

from lib.runcommand import RunCMD

class Specs:

    def __init__(self):
        output = run_dmidecode()
        if not output:
            print("No dmidecode output.")
            return

        self.specs = {
            "vendor": get_manufacturer(output),
            "model": get_model(output),
            "serial": get_serial_number(output),
            "cpu": get_cpu_info(output),
            "ram": f"{self.get_total_memory_gb()} GB",
            "gpu": self.get_gpu_list(),
            "disks": self.getDisks(),
            "resolution": self.getResolution()
            }

    def getSpecs(self):
        return self.specs

    def get_gpu_list(self):
        try:
            output = subprocess.check_output(['lspci'], text=True)
        except subprocess.CalledProcessError as e:
            print("Failed to run lspci:", e)
            return []

        gpus = []
        for line in output.splitlines():
            if re.search(r'VGA compatible controller|3D controller', line, re.IGNORECASE):
                # Split on the first colon after the device class and take the remainder
                parts = line.split(":", 2)
                if len(parts) == 3:
                    gpu_info = parts[2].strip()
                    gpus.append(gpu_info)
                else:
                    # fallback: strip leading PCI address and class manually
                    gpu_info = re.sub(r'^[\da-f:.]+\s+\S+\s+controller:\s*', '', line, flags=re.IGNORECASE)
                    gpus.append(gpu_info.strip())

        return gpus

    def getDisks(self):
        disks = Disks().get()
        return disks

    def detect_lshw_gpus(self):
        if not shutil.which("lshw"):
            return []

        output = RunCMD.run_command('lshw -C display')
        gpus = []

        for line in output.splitlines():
            line = line.strip()
            if line.startswith("product:"):
                model = line.split("product:", 1)[1].strip()
                if model and model.lower() != "unknown":
                    gpus.append(model)
        return gpus

    def get_total_memory_gb(self):
        try:
            with open('/proc/meminfo', 'r') as f:
                for line in f:
                    if line.startswith('MemTotal:'):
                        # Extract value in kB and convert to GB
                        mem_kb = int(line.split()[1])
                        mem_gb = mem_kb / 1024 / 1024
                        return round(mem_gb, 2)
        except Exception as e:
            print("Failed to read memory info:", e)
            return None

    def getResolution(self):
        d = display.Display()
        screen = d.screen()
        width = screen.width_in_pixels
        height = screen.height_in_pixels
        return width, height
