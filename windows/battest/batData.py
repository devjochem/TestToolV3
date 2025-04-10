from lib.batteryinfo import Info


class BatData:

    def __init__(self, bat):
        self.info = Info().getInfo()[bat]

    def getdata(self):
        return self.info