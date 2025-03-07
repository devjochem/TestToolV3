# This Python file uses the following encoding: utf-8

from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import QMainWindow

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from testtool.windows.lcdtest.lcd import Ui_LCDTest

class LCDWindow(QMainWindow):
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

