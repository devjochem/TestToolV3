import logging
import sys

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QMainWindow, QAbstractItemView, QTableWidgetItem, QApplication

from lib.batteryinfo import UPowerManager
from lib.results import generate_report
from lib.systemspecs import Specs
from windows.audiotest.audiotestwindow import AudioTest
from windows.console.console import ConsoleWindow
from windows.dialogs.NameDialog import NameDialog

from windows.lcdtest.lcdtestwindow import LCDWindow
from windows.kbtest.kbtestwindow import KBWindow
from windows.camtest.camtestwindow import CamWindow
from windows.battest.battestwintest import BatWindow

from windows.mainwindow.form import Ui_MainWindow
from windows.touchtest.touchWindow import TouchTester
from windows.visualtest.visualwindow import VisualDialog


def info(key, data):
    info = "<span style=\" font-size:12pt; font-weight:600;\" >"
    info += f"{key}:    "
    info += "<span style=\" font-size:12pt; font-weight:600; color:#28a745;\" >" + f" {data}" + "</span>"
    info += "</span>"
    return info

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.nameWindow = None
        self.report = None
        self.visualWindow = None
        self.audioWindow = None
        self.touchWindow = None
        self.camWindow = None
        self.kbWindow = None
        self.lcdWindow = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.test_results = {
            "LCD": "Not tested",
            "KB": "Not tested",
            "BAT": "Not detected",
            "CAM": "Not tested",
            "AUDIO": "Not tested",
        }

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
        self.ui.reportButton.clicked.connect(lambda p: self.start_report())
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
        self.text.append(info("SERIAL", self.specs['serial']))
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
        if self.lcdWindow is None:
            self.lcdWindow = LCDWindow()
            self.lcdWindow.dataSent.connect(self.receive_data_lcd)
        self.lcdWindow.showFullScreen()

    @Slot(str)
    def receive_data_lcd(self, text):
        self.test_results['LCD'] = text
        self.run_next_test()

    def kbwindow(self):
        if self.kbWindow is None:
            self.kbWindow = KBWindow()
            self.kbWindow.dataSent.connect(self.receive_data_kb)
        self.kbWindow.show()

    @Slot(str)
    def receive_data_kb(self, data):
        self.test_results['KB'] = data
        self.run_next_test()

    def camwindow(self):
        if self.camWindow is None:
            self.camWindow = CamWindow()
            self.camWindow.dataSent.connect(self.receive_data_cam)
        self.camWindow.show()

    @Slot(str)
    def receive_data_cam(self, data):
        self.test_results['CAM'] = data
        self.run_next_test()

    def audiowindow(self):
        if self.audioWindow is None:
            self.audioWindow = AudioTest()
            self.audioWindow.dataSent.connect(self.receive_data_audio)
        self.audioWindow.show()

    @Slot(dict)
    def receive_data_audio(self, data):
        self.test_results['AUDIO'] = data
        self.run_next_test()

    def namewindow(self):
        if self.nameWindow is None:
            self.nameWindow = NameDialog()
            if self.nameWindow.exec():
                data = self.nameWindow.get_input_text()
                self.test_results["NAME"] = data
                self.run_next_test()
            else:
                print("Cancelled")
                self.run_next_test()
        
    def visualwindow(self):
        if self.visualWindow is None:
            self.visualWindow = VisualDialog()
            if self.visualWindow.exec():
                data = self.visualWindow.get_checkbox_data()
                print("Checkbox states:", data)
                self.test_results["VISUAL"] = data
                self.run_next_test()
            else:
                print("Cancelled")
                self.run_next_test()

    def touchwindow(self):
        self.touchWindow = TouchTester()
        self.touchWindow.show()

    def start_report(self):
        self.report = True
        # Define the sequence of test windows to run
        self.test_sequence = [
            self.namewindow,
            self.lcdwindow,
            self.kbwindow,
            self.camwindow,
            self.audiowindow,
            self.visualwindow
        ]
        self.current_test_index = 0
        self.run_next_test()

    def run_next_test(self):
        if self.current_test_index < len(self.test_sequence):
            test_func = self.test_sequence[self.current_test_index]
            self.current_test_index += 1
            test_func()
        else:
            self.finalize_report()

    def finalize_report(self):
        # All tests done — for now, just print results
        upower = UPowerManager()
        healthdata = []
        for device in upower.enumerate_devices():
            if "battery" in device.lower():
                healthdata.append(upower.print_battery_info(device)["Capacity"])
        self.test_results['BAT'] = healthdata
        generate_report(self.test_results['NAME'], self.test_results)

        self.report = False


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())