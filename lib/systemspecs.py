from Xlib import display

from lib.diskinfo import Disks
from lib.readfile import ReadFile

from lib.runcommand import RunCMD

class Specs:

    def __init__(self):
        self.specs = {
            "vendor": ReadFile("/sys/devices/virtual/dmi/id/board_vendor").getdata(),
            "model": ReadFile("/sys/devices/virtual/dmi/id/board_name").getdata(),
            "cpu": RunCMD('echo "$(neofetch --cpu_cores off cpu)"').run_command().replace('cpu:', ''),
            "ram": RunCMD(['echo "$(neofetch memory)"']).run_command().replace('memory:', ''),
            "gpu": RunCMD(['echo "$(neofetch gpu)"']).run_command().splitlines(),
            "disks": self.getDisks(),
            "resolution": self.getResolution()
            }

    def getSpecs(self):
        return self.specs

    def getDisks(self):
        disks = Disks().get()
        return disks

    def getResolution(self):
        d = display.Display()
        screen = d.screen()
        width = screen.width_in_pixels
        height = screen.height_in_pixels
        return width, height
