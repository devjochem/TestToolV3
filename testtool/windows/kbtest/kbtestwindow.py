from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from testtool.windows.kbtest.key import Key, KEY_MAP

from testtool.windows.kbtest.kbtest import Ui_MainWindow

class KBWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        QApplication.instance().installEventFilter(self)

    def keyPressEvent(self, event):
        if isinstance(event, QKeyEvent):
            pkey = event.key()
            #print(event.nativeScanCode())
            self.setColor(pkey,"orange")

    def keyReleaseEvent(self, event):
        if isinstance(event, QKeyEvent):
            pkey = event.key()
            self.setColor(pkey,"green")

    def setColor(self, key, color):
        try:
            btn = KEY_MAP[key]
        except KeyError:
            return
        if str(btn).startswith("Key.LEFT"):
            self.findChild(QLabel, Key["RIGHT" + str(btn).split("Key.LEFT")[1]].value).setStyleSheet(
                f"background-color: {color};  border: 1px solid black;")
        self.findChild(QLabel, Key(btn).value).setStyleSheet(f"background-color: {color};  border: 1px solid black;")
    def getKey(self, num):
        try:
            btn = KEY_MAP[num]
        except KeyError:
            return None
        return self.findChild(QLabel, Key(btn).value)

