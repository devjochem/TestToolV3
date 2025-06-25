import sys
from PySide6.QtWidgets import QApplication, QWidget, QTextEdit, QVBoxLayout, QPushButton
from PySide6.QtCore import QTimer, QIODevice, QBuffer, QObject, Signal
import traceback

class EmittingStream(QObject):
    text_written = Signal(str)

    def write(self, text):
        if text.strip():
            self.text_written.emit(str(text))

    def flush(self):
        pass


class ConsoleWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Console Output")
        self.resize(600, 400)

        self.output_area = QTextEdit(self)
        self.output_area.setReadOnly(True)

        layout = QVBoxLayout()
        layout.addWidget(self.output_area)
        self.setLayout(layout)

        # Redirect stdout and stderr
        sys.stdout = EmittingStream()
        sys.stderr = EmittingStream()

        # Connect signals to text output
        sys.stdout.text_written.connect(self.append_output)
        sys.stderr.text_written.connect(self.append_output)

    def append_output(self, text):
        self.output_area.append(text)