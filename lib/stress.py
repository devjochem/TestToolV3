import logging
import multiprocessing as mp
import subprocess

from PySide6.QtCore import QRunnable, Slot

class Worker(QRunnable):
    """Worker thread."""

    def __init__(self, /):
        super().__init__()
        self.job = None
        self.n_cpu = None
        self.log = logging.getLogger()

    @Slot()
    def run(self):

        self.log.info("Thread start")
        self.n_cpu = round((50 * mp.cpu_count()) / 100.0)
        self.job = subprocess.Popen('stress-ng ' + '-c ' + str(self.n_cpu), shell=True, stdout=subprocess.PIPE,
                                    stderr=subprocess.STDOUT)
        output = self.job.communicate()[0]
        exitCode = self.job.returncode

        if exitCode == 0:
            return output
        else:
            self.log.warning(exitCode, output)


    def kill(self):
        self.job.terminate()