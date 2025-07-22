import sys

from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QDialog, QApplication

from windows.visualtest.visualtest import Ui_VisualCheck

class VisualDialog(QDialog):
    dataSent = Signal(tuple)
    def __init__(self):
        super().__init__()
        self.ui = Ui_VisualCheck()
        self.ui.setupUi(self)
        self.setup_mutual_exclusion()

    def setup_mutual_exclusion(self):
        pairs = [
            (self.ui.backlightBox, self.ui.backheavyBox),
            (self.ui.bezellightBox, self.ui.bezelheavyBox),
            (self.ui.palmlichtBox, self.ui.palmheavyBox),
            (self.ui.sidelightBox, self.ui.sideheavyBox),
            (self.ui.botlightBox, self.ui.botheavyBox),
        ]

        for cb1, cb2 in pairs:
            cb1.stateChanged.connect(lambda state, other=cb2: other.setChecked(False) if state else None)
            cb2.stateChanged.connect(lambda state, other=cb1: other.setChecked(False) if state else None)

    def get_checkbox_data(self):
        pairs = (
            ("back", self.ui.backlightBox, self.ui.backheavyBox),
            ("bezel", self.ui.bezellightBox, self.ui.bezelheavyBox),
            ("palm", self.ui.palmlichtBox, self.ui.palmheavyBox),
            ("side", self.ui.sidelightBox, self.ui.sideheavyBox),
            ("bot", self.ui.botlightBox, self.ui.botheavyBox),
        )

        result = {}
        for name, cb_light, cb_heavy in pairs:
            if cb_light.isChecked():
                status = "Lichte schade"
            elif cb_heavy.isChecked():
                status = "Zware schade"
            else:
                status = "Nette staat"
            result[name] =  status

        return result

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlg = VisualDialog()
    if dlg.exec():
        data = dlg.get_checkbox_data()
        print("Checkbox states:", data)
    else:
        print("Cancelled")