from PySide6.QtWidgets import QDialog, QLineEdit, QPushButton, QVBoxLayout, QLabel, QCheckBox


class AUDIODialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AUDIOTest Result")
        self.resize(200, 100)

        self.left_check = QCheckBox()
        self.right_check = QCheckBox()
        self.mic_check = QCheckBox()
        self.ok_button = QPushButton("OK")
        self.ok_button.clicked.connect(self.accept)# Close dialog with accept()

        self.left_check.setText("Linker Speaker")
        self.right_check.setText("Rechter Speaker")
        self.mic_check.setText("Microfoon")

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Wat werkt er wel/niet?"))
        layout.addWidget(self.left_check)
        layout.addWidget(self.right_check)
        layout.addWidget(self.mic_check)
        layout.addWidget(self.ok_button)
        self.setLayout(layout)

    def get_data(self):
        data = {
            "LEFT_SPEAKER": self.left_check.checkState().value,
            "RIGHT_SPEAKER": self.right_check.checkState().value,
            "MIC": self.mic_check.checkState().value
        }

        return data