# This Python file uses the following encoding: utf-8

# if __name__ == "__main__":
#     pass
from subprocess import Popen, PIPE, DEVNULL
from lib.diskinfo import DiskType, Disk, DiskInfo, size_in_hrf, time_in_hrf

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
        s = self.run_command("sh scripts/getcpu.sh")
        return s

    def getGPU(self):
        s = self.run_command(["sh scripts/getgpu.sh"])
        return s.splitlines()

    def getMemory(self):
        s = self.run_command(["sh scripts/getmemory.sh"])
        return s

    def getVendor(self):
        file = open("/sys/devices/virtual/dmi/id/board_vendor", "r")
        s = file.read()
        file.close()
        return s

    def getModel(self):
        file = open("/sys/devices/virtual/dmi/id/board_name", "r")
        s = file.read()
        file.close()
        return s

    def getDisks(self):
        di = DiskInfo()
        disks = di.get_disk_list(sorting=True)
        return disks
