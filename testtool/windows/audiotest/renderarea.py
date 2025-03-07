import PySide6
from PySide6.QtCore import QMargins, Qt
from PySide6.QtGui import QPainter, QPalette
from PySide6.QtMultimedia import QAudioFormat
from PySide6.QtWidgets import QWidget


class RenderArea(QWidget):
    def __init__(self, parent: PySide6.QtWidgets.QWidget | None = None) -> None:
        super().__init__(parent=parent)
        self.m_level = 0
        self.setBackgroundRole(QPalette.ColorRole.Base)
        self.setAutoFillBackground(True)
        self.setMinimumHeight(30)
        self.setMinimumWidth(200)

    def set_level(self, value):
        self.m_level = value
        self.update()

    def paintEvent(self, event: PySide6.QtGui.QPaintEvent) -> None:
        with QPainter(self) as painter:
            painter.setPen(Qt.GlobalColor.black)
            frame = painter.viewport() - QMargins(10, 10, 10, 10)

            painter.drawRect(frame)

            if self.m_level == 0.0:
                return

            pos: int = round((frame.width() - 1) * self.m_level)
            painter.fillRect(frame.left() + 1, frame.top() + 1, pos, frame.height() - 1,
                             Qt.GlobalColor.red)

class AudioInfo:
    def __init__(self, format: QAudioFormat):
        super().__init__()
        self.m_format = format
        self.m_level = 0.0

    def calculate_level(self, data: bytes, length: int) -> float:
        channel_bytes: int = int(self.m_format.bytesPerSample())
        sample_bytes: int = int(self.m_format.bytesPerFrame())
        num_samples: int = int(length / sample_bytes)

        maxValue: float = 0
        m_offset: int = 0

        for i in range(num_samples):
            for j in range(self.m_format.channelCount()):
                value = 0
                if len(data) > m_offset:
                    data_sample = data[m_offset:]
                    value = self.m_format.normalizedSampleValue(data_sample)
                maxValue = max(value, maxValue)
                m_offset = m_offset + channel_bytes

        return maxValue