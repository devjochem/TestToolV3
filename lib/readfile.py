import logging

class ReadFile:

    def __init__(self, file):
        try:
            file = open(file, "r")
            self.data = file.read()
            file.close()
        except (IOError, OSError) as e:
            log = logging.getLogger()
            log.setLevel(logging.INFO)
            log.warning(f"File {file} not found!")
            self.data = ""

    def getdata(self):
        return self.data