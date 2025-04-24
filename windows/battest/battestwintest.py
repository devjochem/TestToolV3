import logging

from PySide6.QtWidgets import QMainWindow, QErrorMessage
from PySide6.QtCore import QTimer, QThreadPool
import pyqtgraph as pg

from lib.batteryinfo import UPowerManager
from lib.stress import Worker
from lib.timeaxisitem import TimeAxisItem, timestamp
from windows.battest.battest import Ui_MainWindow
from windows.battest.dataviewer.dataviewerwin import DataWindow

def get_data():
    upower = UPowerManager()
    devices = upower.enumerate_devices()
    result = {}

    for device in devices:
        if "battery" in device.lower():
            bats = upower.print_battery_info(device)
            result[device] = bats['Percentage']
    return result

class BatWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.threadpool = None
        self.job = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.log = logging.getLogger()
        self.batlog = logging.getLogger(__name__)
        console_handler = logging.StreamHandler()
        file_handler = logging.FileHandler("batterytest" + str(timestamp()) + ".log", encoding="utf-8")
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
        self.ui.stopButton.clicked.connect(lambda p: self.end_plot())
        self.ui.logviewButton.clicked.connect(lambda p: DataWindow().show())
        self.bats = {}
        colors = [(255,0,0),(0,255,0),(0,255,255)]

        for i,device in enumerate(get_data()):
            if "battery" in device.lower():
                print(device)
                pen = pg.mkPen(color=colors[i])
                data = {'x': [], 'y': []}
                batname = device
                self.bats[batname] = data
                self.bats[batname]['pen'] = self.graphWidget.plot(self.bats[batname]['x'], self.bats[batname]['y'], pen=pen, name=batname)
        self.ui.batteriesInfo.setText(str(len(get_data())))

    def start_plot(self):
        rate = self.ui.rateInfo.text()

        if rate.isdigit():
            if len(self.bats) < 1:
                self.log.error('No batteries found!')
                return
            self.timer.start(int(rate) * 1000)
            self.job = Worker()
            self.threadpool = QThreadPool()
            self.threadpool.start(self.job)
        else:
            error = 'Rate not an integer!'
            self.log.error(error)
            return

    def update_plot_data(self):
        #Get current batteries states
        batteries = get_data()
        for b in batteries:
            battery = self.bats[b]
            x = battery['x']
            y = battery['y']
            cap = float(str(batteries[b]).replace("%", ""))

            #set plot data
            x.append(timestamp())
            y.append(cap)
            battery['pen'].setData(x, y)
            #log battery cap
            self.batlog.info(b + " - " + str(cap))

    def closeEvent(self, event):
        self.end_plot()

    def end_plot(self):
        self.timer.stop()
        if self.job is not None:
            self.job.kill()