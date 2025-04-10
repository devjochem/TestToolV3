import logging

from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import QTimer
import pyqtgraph as pg

from lib.batteryinfo import Info
from lib.timeaxisitem import TimeAxisItem, timestamp
from windows.battest.battest import Ui_MainWindow


class BatWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.log = logging.getLogger()

        self.batlog = logging.getLogger(__name__)
        console_handler = logging.StreamHandler()
        file_handler = logging.FileHandler("batterytest.log", encoding="utf-8")
        formatter = logging.Formatter(
            "{asctime} - {message}",
            style="{",
            datefmt="%Y-%m-%d %H:%M:%S",)
        self.batlog.addHandler(console_handler)
        self.batlog.addHandler(file_handler)
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)
        self.batlog.setLevel(logging.INFO)

        self.graphWidget = pg.PlotWidget(
            title="Battery Graph",
            labels={'left': 'Reading / %'},
            axisItems={'bottom': TimeAxisItem(orientation='bottom')}
        )

        self.ui.graphLayout.addWidget(self.graphWidget)

        self.graphWidget.addLegend()
        self.graphWidget.setBackground('black')

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_plot_data)
        self.ui.startButton.clicked.connect(lambda p: self.start_plot())
        self.ui.stopButton.clicked.connect(lambda p: self.timer.stop())
        self.bats = {}
        colors = [(255,0,0),(0,255,0),(0,255,255)]

        for i,b in enumerate(Info().getInfo()):
            pen = pg.mkPen(color=colors[i])
            data = {'x': [], 'y': []}
            self.bats['BAT' + str(i)] = data
            self.bats['BAT' + str(i)]['pen'] = self.graphWidget.plot(self.bats['BAT' + str(i)]['x'], self.bats['BAT' + str(i)]['y'], pen=pen, name="BAT" + str(i))

        self.ui.batteriesInfo.setText(str(len(Info().getInfo())))

    def start_plot(self):
        rate = self.ui.rateInfo.text()

        if rate.isdigit():
            if len(self.bats) < 1:
                self.log.error('No batteries found!')
                return
            self.timer.start(int(rate) * 1000)
        else:
            self.log.error('Rate not an integer!')
            return

    def update_plot_data(self):
        #Get current batteries states
        batteries = Info().getInfo()
        for i,b in enumerate(batteries):
            battery = self.bats[b]
            x = battery['x']
            y = battery['y']
            time = timestamp()
            cap = int(batteries['BAT' + str(i)]['capacity'])

            x.append(time)
            y.append(cap)
            battery['pen'].setData(x, y)

            self.batlog.info('BAT' + str(i) + " - " + str(cap))

    def closeEvent(self, event):
        self.timer.stop()