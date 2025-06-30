import sys
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtGui import QPainter, QPen, QColor
from PySide6.QtCore import Qt, QPointF, QEvent


class TouchPoint:
    def __init__(self, pos: QPointF):
        self.pos = pos


class TouchTester(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Touchscreen Tester")
        self.setWindowState(Qt.WindowFullScreen)
        self.setAttribute(Qt.WA_AcceptTouchEvents)
        self.setAttribute(Qt.WA_StaticContents)
        self.touch_points = []

    def event(self, event):
        if event.type() == QEvent.TouchBegin or event.type() == QEvent.TouchUpdate:
            self.touch_points = [TouchPoint(p.pos()) for p in event.touchPoints()]
            self.update()
            return True
        elif event.type() == QEvent.TouchEnd:
            self.touch_points.clear()
            self.update()
            return True
        return super().event(event)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        pen = QPen(Qt.red, 10)
        painter.setPen(pen)

        for point in self.touch_points:
            painter.drawPoint(point.pos)
            painter.drawText(point.pos + QPointF(10, -10), f"({int(point.pos.x())}, {int(point.pos.y())})")

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    tester = TouchTester()
    tester.show()
    sys.exit(app.exec())