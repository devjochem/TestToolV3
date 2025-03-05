import numpy as np
from PySide6.QtCore import QThread, Signal

class VideoThread(QThread):
    change_pixmap_signal = Signal(np.ndarray)
    def __init__(self, stream):
        super().__init__()
        self.cap = stream

        self.running = True

    def run(self):
        while self.running:
            ret, cv_img = self.cap.read()
            if ret:
                self.change_pixmap_signal.emit(cv_img)

    def release(self):
        self.cap.release()