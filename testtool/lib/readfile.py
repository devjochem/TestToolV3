class ReadFile:

    def __init__(self, file):
        file = open(file, "r")
        self.data = file.read()
        file.close()

    def getdata(self):
        return self.data