import logging
import os
import sys
from datetime import datetime
from pathlib import Path

from PySide6.QtWidgets import QMainWindow, QApplication, QFileDialog
import pyqtgraph as pg

from lib.timeaxisitem import TimeAxisItem, timestamp
from windows.battest.dataviewer.dataviewer import Ui_MainWindow


class DataWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.log = logging.getLogger()

        self.graphWidget = pg.PlotWidget(
            title="Battery Graph",
            labels={'left': 'Reading / %'},
            axisItems={'bottom': TimeAxisItem(orientation='bottom')}
        )

        self.ui.gridLayout.addWidget(self.graphWidget)

        self.graphWidget.addLegend()
        self.graphWidget.setBackground('black')

        self.bats = {}

        self.ui.pushButton.clicked.connect(lambda p: self.open_file_dialog())

    def start_plot(self, data):
        colors = [(255,0,0),(0,255,0),(0,255,255)]
        self.bats.clear()

        text = self.ui.dataOutput
        for line in data:
            data = line.split(" - ")

            datetime_object = datetime.strptime(data[0], "%Y-%m-%d %H:%M:%S")
            time = datetime_object.timestamp()
            bat = data[1]
            cap = float(data[2].replace('\n', ''))

            if not self.bats.keys().__contains__(bat):
                id = ''.join(x for x in bat if x.isdigit())
                pen = pg.mkPen(color=colors[int(id)])
                data = {'x': [], 'y': []}
                self.bats[bat] = data
                self.bats[bat]['pen'] = self.graphWidget.plot(self.bats[bat]['x'],
                                                                         self.bats[bat]['y'], pen=pen,
                                                                         name=bat)

            battery = self.bats[bat]
            x = battery['x']
            y = battery['y']

            x.append(time)
            y.append(cap)
            battery['pen'].setData(x, y)

        for bat in self.bats:
            first, *_, last = self.bats[bat]['x']
            first = datetime.fromtimestamp(first)
            last = datetime.fromtimestamp(last)
            text.append('Log Info ' + bat)
            text.append('  Start: ' + str(first))
            text.append('  End: ' + str(last))
            text.append('')
            text.append('  Duration: ' + str(last - first))
            text.append('')
            text.append('')

        print(self.bats)



    def open_file_dialog(self):
        filename, ok = QFileDialog.getOpenFileName(
            self,
            "Select a File",
            str(os.getenv('HOME')),
            "Battery Log (*.log)"
        )
        if filename:
            path = Path(filename)
            with open(path, 'r') as file:
                 self.start_plot(file.readlines())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = DataWindow()
    w.show()
    sys.exit(app.exec())

