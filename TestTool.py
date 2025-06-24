import sys
import time

from PySide6.QtWidgets import QApplication
from windows.mainwindow.mainwindow import MainWindow, self_update
import sys

def main():
    if "--check-update" in sys.argv:
        self_update()
    else:
        print("Running main application.")
        # Your app logic here
        time.sleep(2)
        print("Main app done.")
        app = QApplication(sys.argv)
        widget = MainWindow()
        widget.show()
        sys.exit(app.exec())

if __name__ == "__main__":
    main()