# This Python file uses the following encoding: utf-8

# if __name__ == "__main__":
#     pass
import os
class Info:

    def __init__(self):
        self.info = {}
        self.getBatdata()

    def getInfo(self):
        return self.info

    def listBat(self):
        dir = os.listdir("/sys/class/power_supply/")
        return sum('BAT' in s for s in dir)

    def read_file(self, file):
        file = open(file, "r")
        s = file.read()
        file.close()
        return s


    def getBatdata(self):
        for i in range(self.listBat()):
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
                data[d] = self.read_file(basedir + d).replace("\n", "")
            data["health"] = int(data["charge_full"])*100 // int(data["charge_full_design"])
            print(data["health"])
            print(data)
            self.info["BAT" + str(i)] = data
