from PySide6.QtWidgets import QDialog, QLineEdit, QPushButton, QVBoxLayout, QLabel


class NameDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Naam")
        self.resize(200, 100)

        self.input_field = QLineEdit()
        self.ok_button = QPushButton("OK")
        self.ok_button.clicked.connect(self.accept)  # Close dialog with accept()

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Naam:"))
        layout.addWidget(self.input_field)
        layout.addWidget(self.ok_button)
        self.setLayout(layout)

    def get_input_text(self):
        return self.input_field.text()