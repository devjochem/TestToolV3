from subprocess import Popen, PIPE, DEVNULL

from testtool.lib.diskinfo import DiskInfo
from testtool.lib.readfile import ReadFile


class Specs:

    def __init__(self):
        self.specs = {
            "vendor": self.getVendor(),
            "model": self.getModel(),
            "cpu": self.getCPU(),
            "ram": self.getMemory(),
            "gpu": self.getGPU(),
            "disks": self.getDisks()
            }


    def getSpecs(self):
        return self.specs

    def run_command(self, command):
        process = Popen(command, stdout=PIPE, universal_newlines=True, shell=True,stderr=DEVNULL)
        stdout, stderr = process.communicate()
        del stderr
        return stdout

    def getCPU(self):
        s = self.run_command("sh testtool/scripts/getcpu.sh")
        return s

    def getGPU(self):
        s = self.run_command(["sh testtool/scripts/getgpu.sh"])
        return s.splitlines()

    def getMemory(self):
        s = self.run_command([f"sh testtool/scripts/getmemory.sh"])
        return s

    def getVendor(self):
        return ReadFile("/sys/devices/virtual/dmi/id/board_vendor").getdata()

    def getModel(self):
        return ReadFile("/sys/devices/virtual/dmi/id/board_name").getdata()

    def getDisks(self):
        di = DiskInfo()
        disks = di.get_disk_list(sorting=True)
        return disks
