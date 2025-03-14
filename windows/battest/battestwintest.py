from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtCore import QTimer
import pyqtgraph as pg
import sys
from random import randint

from pyparsing import Empty

from lib.batteryinfo import Info
from windows.battest.battest import Ui_MainWindow


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        self.graphWidget = pg.PlotWidget()
        self.ui.graphLayout.addWidget(self.graphWidget)

        self.x = list(range(100))  # 100 time points
        self.y = []  # 100 data points

        batteries = Info().getInfo()
        self.bcount = 0
        for b in batteries:
            self.bcount += 1

        self.ui.batteriesInfo.setText(str(self.bcount))
        self.graphWidget.setBackground('w')

        pen = pg.mkPen(color=(255, 0, 0))
        self.data_line =  self.graphWidget.plot(self.x, self.y, pen=pen)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_plot_data)
        self.ui.startButton.clicked.connect(lambda p: self.start_plot())
        self.ui.stopButton.clicked.connect(lambda p: self.timer.stop())

        #self.timer.start()
    def is_int(self, data):
        if data.isdigit():
            return int(data)
        else:
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('Rate must be an int!')
            error_dialog.show()

    def start_plot(self):
        data = self.ui.rateInfo.text()
        if data.isdigit():
            batteries = Info().getInfo()
            if batteries is not Empty:
                print('No batteries!')
                return
            self.timer.start(data)
        else:
            print('Rate not an integer!')
            return

    def update_plot_data(self):
        self.x.append(self.x[-1] + 1)
        batteries = Info().getInfo()
        self.y.append(batteries[0]['Charge'])  # Add the battery percentage

        self.data_line.setData(self.x, self.y)


app = QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec())