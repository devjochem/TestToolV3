# This Python file uses the following encoding: utf-8

from PySide6.QtWidgets import QMainWindow, QAbstractItemView, QTableWidgetItem
from lib.systemspecs import Specs
from lib.batteryinfo import Info
from windows.audiotest.audiotestwindow import AudioTest

from windows.lcdtest.lcdtestwindow import LCDWindow
from windows.kbtest.kbtestwindow import KBWindow
from windows.camtest.camtestwindow import CamWindow

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from form import Ui_MainWindow


def info(key, data):
    info = "<span style=\" font-size:12pt; font-weight:600;\" >"
    info += f"{key}:    "
    info += "<span style=\" font-size:12pt; font-weight:600; color:#28a745;\" >" + f" {data}" + "</span>"
    info += "</span>"
    return info


def widgetdefaults(w):
    w.setEditTriggers(QAbstractItemView.NoEditTriggers)
    #w.verticalHeader().setVisible(False)
    w.horizontalHeader().setStretchLastSection(True)


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_lcd.clicked.connect(lambda p: self.lcdwindow())
        self.ui.pushButton_kb.clicked.connect(lambda p: self.kbwindow())
        self.ui.pushButton_cm.clicked.connect(lambda p: self.camwindow())
        self.ui.pushButton_2.clicked.connect(lambda p: self.audiowindow())
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
        widgetdefaults(table)
        table.setHorizontalHeaderLabels(('Model', 'Size', 'Type'))

        for i,d in enumerate(disks):
            if d.get_type() == 'LOOP':
                continue
            s, u = d.get_size_in_hrf()
            table.setItem(i, 0, QTableWidgetItem(d.get_model()))
            table.setItem(i, 1, QTableWidgetItem(f"{s:.1f}  {u} "))
            table.setItem(i, 2, QTableWidgetItem(d.get_type_str()))
        table.resizeColumnsToContents()

    def populate_bat(self):
        batteries = Info().getInfo()
        if len(batteries) == 0:
            return
        #table = self.getTable("batteryTable", 11, len(batteries))
        table = self.ui.batteryTable
        table.setRowCount(9)
        table.setColumnCount(len(batteries))

        table.setHorizontalHeaderLabels(('Battery 1', 'Battery 2', 'Battery 3'))
        table.setVerticalHeaderLabels(('Charge', 'Health', 'Charge Full', 'Charge Full Design', 'Cycle Count', 'Voltage', 'Voltage Min', 'Manufacturer', 'Model'))
        order = ["capacity","health","charge_full","charge_full_design","cycle_count","voltage_now","voltage_min_design","manufacturer","model_name"]

        widgetdefaults(table)

        for i,bat in enumerate(batteries):
            for o,item in enumerate(order):
                table.setItem(o, i, QTableWidgetItem(str(batteries[bat][item])))
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
        self.populate_bat()
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

    def audiowindow(self):
        self.audioWindow = AudioTest()
        self.audioWindow.show()