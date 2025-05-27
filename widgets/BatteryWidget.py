from PySide6.QtCore import QAbstractTableModel, Qt, QTimer
from PySide6.QtWidgets import QTableView, QWidget, QVBoxLayout, QApplication
from lib.batteryinfo import UPowerManager

def getData():
    upower = UPowerManager()
    devices = upower.enumerate_devices()
    battery_data = {}

    for device in devices:
        if "battery" in device.lower():
            info = upower.print_battery_info(device)
            battery_data[device] = info

    if not battery_data:
        return [], []

    # Use keys from first battery as row labels
    row_labels = list(next(iter(battery_data.values())).keys())
    column_headers = list(battery_data.keys())

    print(row_labels)
    print(column_headers)

    # Each row is a battery property (e.g., state), values go across batteries
    table = []
    for row_label in row_labels:
        row = [battery_data[dev][row_label] for dev in column_headers]
        table.append(row)

    return column_headers, table, row_labels


class TableModel(QAbstractTableModel):
    def __init__(self):
        super().__init__()
        self._headers, self._data, self._row_labels = getData()

    def rowCount(self, index):
        return len(self._row_labels)

    def columnCount(self, index):
        return len(self._headers)

    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self._data[index.row()][index.column()]

    def headerData(self, section, orientation, role):
        if role != Qt.DisplayRole:
            return None
        if orientation == Qt.Horizontal:
            return self._headers[section].split('/')[-1]  # just device name
        else:
            return self._row_labels[section]

class BatWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.view = QTableView()
        self.model = TableModel()
        self.view.setModel(self.model)

        layout = QVBoxLayout()
        layout.addWidget(self.view)
        self.setLayout(layout)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.refresh_data)
        self.timer.start(2000)

    def refresh_data(self):
        self.model = TableModel()
        self.view.setModel(self.model)
