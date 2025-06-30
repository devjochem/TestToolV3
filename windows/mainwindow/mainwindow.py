# This Python file uses the following encoding: utf-8
import logging
import sys
from PySide6.QtWidgets import QMainWindow, QAbstractItemView, QTableWidgetItem, QApplication

from lib.systemspecs import Specs
from windows.audiotest.audiotestwindow import AudioTest
from windows.console.console import ConsoleWindow

from windows.lcdtest.lcdtestwindow import LCDWindow
from windows.kbtest.kbtestwindow import KBWindow
from windows.camtest.camtestwindow import CamWindow
from windows.battest.battestwintest import BatWindow

from windows.mainwindow.form import Ui_MainWindow
from windows.touchtest.touchWindow import TouchTester


def info(key, data):
    info = "<span style=\" font-size:12pt; font-weight:600;\" >"
    info += f"{key}:    "
    info += "<span style=\" font-size:12pt; font-weight:600; color:#28a745;\" >" + f" {data}" + "</span>"
    info += "</span>"
    return info

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        logging.basicConfig(filename="./AppLog.log",
                            format='%(asctime)s - %(levelname)s - %(message)s',
                            filemode='w')
        log = logging.getLogger()
        log.setLevel(logging.INFO)


        self.ui.pushButton_lcd.clicked.connect(lambda p: self.lcdwindow())
        self.ui.pushButton_kb.clicked.connect(lambda p: self.kbwindow())
        self.ui.pushButton_cm.clicked.connect(lambda p: self.camwindow())
        self.ui.pushButton_2.clicked.connect(lambda p: AudioTest().show())
        self.ui.batButton.clicked.connect(lambda p: BatWindow().show())
        #self.ui.actionUpdate.triggered.connect(lambda p: self_update())
        #self.ui.actionConsole.triggered.connect(lambda p: ConsoleWindow().show())
        self.ui.pushButton_ts.clicked.connect(lambda p: self.touchwindow())
        log.info("TestTool started")
        specs = Specs()
        self.specs = specs.getSpecs()
        self.useroutput()

    def infolist(self,output,key,l):
        self.text = output
        info = "<span style=\" font-size:12pt; font-weight:600;\" >"
        info += f"{key}:"
        info += "</span>"
        self.text.append(info)
        for i,s in enumerate(l):
            self.text.append("<span style=\" font-size:12pt; font-weight:600; color:#28a745;\" >" + s.replace('gpu: ', '') + "</span><br>")

    def populate_disks(self):
        disks = self.specs["disks"]
        table = self.ui.diskTable
        table.verticalHeader().setVisible(False)
        table.setRowCount(len(disks))
        table.setColumnCount(3)
        table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        table.horizontalHeader().setStretchLastSection(True)
        table.setHorizontalHeaderLabels(('Model', 'Size', 'Type'))
        for i,disk in enumerate(disks):
            table.setItem(i, 0, QTableWidgetItem(disk['model']))
            table.setItem(i, 1, QTableWidgetItem(f"{disk['size_gb']} GB"))
            table.setItem(i, 2, QTableWidgetItem(disk['type']))
        table.resizeColumnsToContents()

    def useroutput(self):
        self.text = self.ui.userOutput
        title = "<span style=\" font-size:32pt; font-weight:600;\" > System Info </span>"
        self.text.append(title)

        self.text.append(info("VENDOR", self.specs['vendor']))
        self.text.append(info("MODEL", self.specs['model']))
        self.text.append(info("CPU", self.specs['cpu']))
        self.text.append(info("RAM", self.specs['ram']))

        self.text.append(info("Screen Res", self.specs['resolution']))
        gpus = self.specs["gpu"]
        self.infolist(self.text,"GPU(S)",gpus)
        self.populate_disks()
        #self.text.append(f'   {self.specs["cpu"]}')
        return self.text

    def consolewindow(self):
        self.consoleWindow = ConsoleWindow()
        self.consoleWindow.show()

    def lcdwindow(self):
        self.lcdWindow = LCDWindow()
        self.lcdWindow.show()
        self.lcdWindow.showFullScreen()

    def kbwindow(self):
        self.kbWindow = KBWindow()
        self.kbWindow.show()

    def camwindow(self):
        self.camWindow = CamWindow()
        self.camWindow.show()

    def touchwindow(self):
        self.touchWindow = TouchTester()
        self.touchWindow.show()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())