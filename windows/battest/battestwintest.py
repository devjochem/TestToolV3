from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtCore import QTimer
import pyqtgraph as pg
import sys

from lib.batteryinfo import Info
from windows.battest.battest import Ui_MainWindow


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.graphWidget = pg.PlotWidget()
        self.ui.graphLayout.addWidget(self.graphWidget)

        self.graphWidget.setBackground('w')

        self.bats = {}

        batteries = Info().getInfo()
        for i,b in enumerate(batteries):
            pen = pg.mkPen(color=(255, i * 50, 0))
            data = {'x': [], 'y': []}
            self.bats['BAT' + str(i)] = data
            self.bats['BAT' + str(i)]['pen'] = self.graphWidget.plot(self.bats['BAT' + str(i)]['x'], self.bats['BAT' + str(i)]['y'], pen=pen, name=f"BAT{str(i)}")

        self.ui.batteriesInfo.setText(str(len(self.bats)))
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_plot_data)
        self.ui.startButton.clicked.connect(lambda p: self.start_plot())
        self.ui.stopButton.clicked.connect(lambda p: self.timer.stop())
        self.bats = {}
        batteries = Info().getInfo()

        for i,b in enumerate(batteries):
            pen = pg.mkPen(color=(255, i * 50, 0))
            data = {'x': [], 'y': []}
            self.bats['BAT' + str(i)] = data
            self.bats['BAT' + str(i)]['pen'] = self.graphWidget.plot(self.bats['BAT' + str(i)]['x'], self.bats['BAT' + str(i)]['y'], pen=pen)



    def start_plot(self):
        data = self.ui.rateInfo.text()
        if data.isdigit():
            if len(self.bats) < 1:
                print('No batteries!')
                return
            self.timer.start(int(data))
        else:
            print('Rate not an integer!')
            return

    def update_plot_data(self):
        batteries = Info().getInfo()
        for i,b in enumerate(self.bats):
            battery = self.bats[b]
            x = battery['x']
            y = battery['y']

            if len(x) < 1:
                x.append(0)
            else:
                x.append(x[-1] + 1)
            y.append(int(batteries['BAT0']['capacity']))

            pg.PlotItem.addLegend()
            battery['pen'].setData(x, y)


app = QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec())