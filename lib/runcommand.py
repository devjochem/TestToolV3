from subprocess import Popen, PIPE, DEVNULL

class RunCMD:

    def __init__(self, command):
        self.command = command
        self.run_command()

    def run_command(self):
        process = Popen(self.command, stdout=PIPE, universal_newlines=True, shell=True, stderr=DEVNULL)
        stdout, stderr = process.communicate()
        del stderr
        return stdout
