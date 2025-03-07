# This Python file uses the following encoding: utf-8

# if __name__ == "__main__":
#     pass
import os
from testtool.lib.readfile import ReadFile

class Info:

    def __init__(self):
        self.info = {}
        self.getBatdata()

    def getInfo(self):
        return self.info

    def getBatdata(self):
        for i in range(sum('BAT' in s for s in os.listdir("/sys/class/power_supply/"))):
            basedir = f"/sys/class/power_supply/BAT{i}/"
            data = {"charge_full": "",
            "charge_full_design": "",
            "capacity": "",
            "capacity_level": "",
            "charge_now": "",
            "cycle_count": "",
            "manufacturer": "",
            "model_name": "",
            "voltage_now": "",
            "voltage_min_design": ""}
            for d in data.keys():
                data[d] = ReadFile(basedir + d).getdata().replace("\n", "")
            data["health"] = int(data["charge_full"])*100 // int(data["charge_full_design"])
            self.info["BAT" + str(i)] = data
