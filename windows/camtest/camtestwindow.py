import sys

import numpy as np
from PySide6 import QtGui
from PySide6.QtCore import Qt, Slot
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow,QPushButton
from windows.camtest.video import VideoThread
import cv2

from windows.camtest.camtest import Ui_MainWindow

class CamWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.thread = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        QApplication.instance().installEventFilter(self)
        self.image_label = self.ui.label

        self.cameras = []
        for i in range(0,5):
            if self.testDevice(i) is None:
                continue
            self.cameras.append(i)
            print(f"Found camera {i}!")
        for cam in self.cameras:
            btn = self.findChild(QPushButton, "btnCam" + str(cam))
            btn.setEnabled(True)
            btn.clicked.connect(lambda p: self.changecam(cam))

    def startThread(self, index):
        self.thread = VideoThread(cv2.VideoCapture(self.cameras[index]))
        self.thread.change_pixmap_signal.connect(self.update_image)
        self.thread.start()

    def activated(self, index):
        self.startThread(index)

    def changecam(self, index):
        if self.thread is None:
            self.startThread(index)
            return
        self.thread.release()
        self.thread.exit(0)
        self.startThread(index)

    def testDevice(self, source):
        cap = cv2.VideoCapture(source)
        if cap is None or not cap.isOpened():
            return None
        cap.release()
        return source

    def closeEvent(self, event):
        if self.thread is None:
            print("Thread is none!")
            return
        self.thread.release()
        self.thread.exit(0)
        event.accept()

    @Slot(np.ndarray)
    def update_image(self, cv_img):
        """Updates the image_label with a new opencv image"""
        qt_img = self.convert_cv_qt(cv_img)
        self.image_label.setPixmap(qt_img)

    def convert_cv_qt(self, cv_img):
        """Convert from an opencv image to QPixmap"""
        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        p = convert_to_Qt_format.scaled(w, h, Qt.KeepAspectRatio)
        return QPixmap.fromImage(p)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    a = CamWindow()
    a.show()
    sys.exit(app.exec_())