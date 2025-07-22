# This Python file uses the following encoding: utf-8
from PySide6.QtCore import Signal
from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import QMainWindow

from windows.lcdtest.LCDDialog import LCDDialog
from windows.lcdtest.lcd import Ui_LCDTest

class LCDWindow(QMainWindow):
    dataSent = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_LCDTest()
        self.ui.setupUi(self)

        self.colors = ["green", "blue", "black", "white", "red"]
        self.setStyleSheet("background-color: red;")

    def keyPressEvent(self, event):
        if isinstance(event, QKeyEvent):
            pkey = event.key()
            if pkey.real == 16777216:
                self.close()
            elif pkey.real == 32:
                self.change_color()

    def change_color(self):
        color = self.colors.pop(0)
        self.colors.append(color)
        self.setStyleSheet(f"background-color: {color};")

    def closeEvent(self, event):
        dialog = LCDDialog()
        if dialog.exec():  # This runs the dialog modally and blocks until closed
            text = dialog.get_input_text()
            self.send_data(text)
        else:
            self.send_data("Test canceled.")

    def send_data(self, data):
        self.dataSent.emit(data)

