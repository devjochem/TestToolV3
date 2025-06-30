import sys
import time

from PySide6.QtWidgets import QApplication
from windows.mainwindow.mainwindow import MainWindow
import sys

def main():
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()