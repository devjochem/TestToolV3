# This Python file uses the following encoding: utf-8
import logging
import sys

from PySide6.QtWidgets import QMainWindow, QAbstractItemView, QTableWidgetItem, QApplication
from lib.systemspecs import Specs
from windows.audiotest.audiotestwindow import AudioTest

from windows.lcdtest.lcdtestwindow import LCDWindow
from windows.kbtest.kbtestwindow import KBWindow
from windows.camtest.camtestwindow import CamWindow
from windows.battest.battestwintest import BatWindow

from windows.mainwindow.form import Ui_MainWindow


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
        # w.verticalHeader().setVisible(False)
        table.horizontalHeader().setStretchLastSection(True)
        table.setHorizontalHeaderLabels(('Model', 'Size', 'Type'))

        for i,d in enumerate(disks):
            if d.get_type_str() == 'LOOP':
                continue
            s, u = d.get_size_in_hrf()
            table.setItem(i, 0, QTableWidgetItem(d.get_model()))
            table.setItem(i, 1, QTableWidgetItem(f"{s:.1f}  {u} "))
            table.setItem(i, 2, QTableWidgetItem(d.get_type_str()))
        table.resizeColumnsToContents()

    def useroutput(self):
        self.text = self.ui.userOutput
        title = "<span style=\" font-size:32pt; font-weight:600;\" > System Info </span>"
        self.text.append(title)

        self.text.append(info("VENDOR", self.specs['vendor']))
        self.text.append(info("MODEL", self.specs['model']))
        self.text.append(info("CPU", self.specs['cpu']))
        self.text.append(info("RAM", self.specs['ram']))

        gpus = self.specs["gpu"]
        self.infolist(self.text,"GPU(S)",gpus)
        self.populate_disks()
        #self.text.append(f'   {self.specs["cpu"]}')
        return self.text


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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())