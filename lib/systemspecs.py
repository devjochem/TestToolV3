from lib.diskinfo import DiskInfo
from lib.readfile import ReadFile

from lib.runcommand import RunCMD

class Specs:

    def __init__(self):
        self.di = DiskInfo()
        self.specs = {
            "vendor": ReadFile("/sys/devices/virtual/dmi/id/board_vendor").getdata(),
            "model": ReadFile("/sys/devices/virtual/dmi/id/board_name").getdata(),
            "cpu": RunCMD('echo "$(neofetch --cpu_cores off cpu)"').run_command().replace('cpu:', ''),
            "ram": RunCMD(['echo "$(neofetch memory)"']).run_command().replace('memory:', ''),
            "gpu": RunCMD(['echo "$(neofetch gpu)"']).run_command().splitlines(),
            "disks": self.getDisks()
            }

    def getSpecs(self):
        return self.specs

    def getDisks(self):
        disks = self.di.get_disk_list(sorting=True)
        return disks
