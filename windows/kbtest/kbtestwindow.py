from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QMessageBox
from PySide6.QtCore import Signal, QObject

from Xlib import X, display
from Xlib.ext import record
from Xlib.protocol import rq
from threading import Thread

from windows.kbtest import key
from windows.kbtest.kbtest import Ui_MainWindow


class KeyEventEmitter(QObject):
    key_event = Signal(str, str)

class KBWindow(QMainWindow):

    dataSent = Signal(bool)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.keymap = key.KEY_MAP

        self.d = display.Display()
        self.emitter = KeyEventEmitter()
        QApplication.instance().installEventFilter(self)
        self.stop_recording_flag = False
        self.ctx = None

        self.emitter.key_event.connect(self.on_key_event)

        self.record_thread = Thread(target=self.start_recording, daemon=True)
        self.record_thread.start()

    def start_recording(self):
        d = display.Display()  # Open display in this thread
        self.ctx = d.record_create_context(
            0,
            [record.AllClients],
            [{
                'core_requests': (0, 0),
                'core_replies': (0, 0),
                'ext_requests': (0, 0, 0, 0),
                'ext_replies': (0, 0, 0, 0),
                'delivered_events': (X.KeyPress, X.KeyRelease),
                'device_events': (X.KeyPress, X.KeyRelease),
                'errors': (0, 0),
                'client_started': False,
                'client_died': False,
            }]
        )

        def _callback(reply):
            if self.stop_recording_flag:
                d.record_disable_context(self.ctx)
                d.flush()
                return
            self.process_event(reply)

        d.record_enable_context(self.ctx, _callback)
        d.record_free_context(self.ctx)


    def process_event(self, reply):
        if reply.category != record.FromServer:
            return
        if reply.client_swapped:
            return
        data = reply.data
        while len(data):
            event, data = rq.EventField(None).parse_binary_value(data, self.d.display, None, None)
            if event.type == X.KeyPress or event.type == X.KeyRelease:
                event_type = "pressed" if event.type == X.KeyPress else "released"
                keysym = self.d.keycode_to_keysym(event.detail, 0)
                if keysym is None:
                    key_name = "Unknown"
                else:
                    key_name = self.keymap.get(str(keysym), f"Unknown keysym {keysym}")
                # Emit signal to update UI on the main thread
                self.emitter.key_event.emit(key_name, event_type)

    def on_key_event(self, key_name, event_type):
        self.setColor(event_type, key_name)


    def setColor(self, event_type, key_name):
        try:
            btn = "btn" + str(key_name).upper()
        except KeyError:
            return
        match event_type:
            case "pressed":
                color = "orange"
            case "released":
                color = "green"
        self.findChild(QLabel, btn).setStyleSheet(f"background-color: {color};  border: 1px solid black;")

    def closeEvent(self, event):
        # Call your custom function here
        self.on_close()

        # Optionally, confirm the close with the user
        reply = QMessageBox.question(
            self,
            "KB Results",
            "Werkt het toetsenbord goed?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No,
        )

        if reply == QMessageBox.Yes:
            self.send_data(True)
            event.accept()
        else:
            self.send_data(False)
            event.accept()

    def on_close(self):
        self.d.record_disable_context(self.ctx)
        self.d.flush()

    def send_data(self, data):
        self.dataSent.emit(data)
