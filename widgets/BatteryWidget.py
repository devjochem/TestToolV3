from PySide6.QtCore import QAbstractTableModel, Qt, QTimer
from PySide6.QtWidgets import QTableView

from lib.batteryinfo import UPowerManager

def getData():
    upower = UPowerManager()
    devices = upower.enumerate_devices()
    headers = []
    table = []
    data = None

    for device in devices:
        if "battery" in device.lower():
            bats = upower.print_battery_info(device)
            data = []
            for key in bats:
                if len(headers) != len(bats):
                    headers.append(key)
                data.append(bats[key])
    table += [data]

    return headers, table

class TableModel(QAbstractTableModel):
    def __init__(self):
        super().__init__()
        self._headers ,self._data = getData()

    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self._data[index.column()][index.row()]

    def headerData(self, col, orientation, role):
        if orientation == Qt.Vertical and role == Qt.DisplayRole:
            return self._headers[col]
        elif orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return "BAT" + str(col)
    def rowCount(self, index):
        if self._data[0] is None:
            return 0
        return len(self._data[0])
    def columnCount(self, index):
        if self._data[0] is None:
            return 0
        return len(self._data)

class BatWidget(QTableView):
    def __init__(self, parent):
        super().__init__(parent=parent)

        self.model = TableModel()
        self.setModel(self.model)

        if self.model.hasIndex(0,0):
            self.timer = QTimer(self)
            self.timer.timeout.connect(self.show_data)
            self.timer.start(2000)

    def show_data(self):
        self.model = TableModel()
        self.setModel(self.model)