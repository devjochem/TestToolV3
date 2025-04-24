import sys

from PySide6.QtCore import Slot, QByteArray, qWarning, QFile, QIODevice
from PySide6.QtMultimedia import QAudioDevice, QAudioFormat, QAudioSource, QAudio, QMediaDevices, QAudioSink
from PySide6.QtWidgets import QApplication, QMainWindow

from windows.audiotest.audiotest import Ui_MainWindow
from windows.audiotest.renderarea import RenderArea, AudioInfo



class AudioTest(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.m_devices = QMediaDevices(self)
        self.m_device = self.m_devices.defaultAudioOutput()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        QApplication.instance().installEventFilter(self)
        self.setup_mic()
        self.setup_out()

    def setup_out(self):
        default_device_info = QMediaDevices.defaultAudioOutput()
        self.ui.comboBox_2.addItem(
            default_device_info.description(), default_device_info
        )

        self.ui.comboBox_2.activated[int].connect(self.output_device_changed)
        for device_info in self.m_devices.audioOutputs():
            if device_info != default_device_info:
                self.ui.comboBox_2.addItem(device_info.description(), device_info)

        self.ui.ma_volume_slider.valueChanged.connect(self.volume_changed)
        self.ui.pushButton.clicked.connect(lambda p: self.initialize_audio('Left'))
        self.ui.pushButton_2.clicked.connect(lambda p: self.initialize_audio('Right'))

    def initialize_audio(self, channel):
        self.m_format = QAudioFormat()
        self.m_format.setSampleRate(48000)
        self.m_format.setChannelCount(1)
        self.m_format.setSampleFormat(QAudioFormat.SampleFormat.Int16)

        info = self.m_devices.audioOutputs()[0]
        if not info.isFormatSupported(self.m_format):
            qWarning("Default format not supported - trying to use nearest")
            self.m_format = info.nearestFormat(self.m_format)

        self.m_audioSink = QAudioSink(self.m_device, self.m_format)
        soundFile= QFile()
        soundFile.setFileName(f"/usr/share/sounds/alsa/Front_{channel}.wav")
        soundFile.open(QIODevice.OpenModeFlag.ReadOnly, )
        self.m_audioSink.start(soundFile)
        #self.ui.ma_volume_slider.setValue(self.m_audioSink.volume() * 100)
        #self.ui.ma_volume_slider.setValue(self.m_audioSink. * 100)


    def setup_mic(self):
        self.m_canvas = RenderArea(self)
        self.ui.micLevels.addWidget(self.m_canvas)

        default_device_info = QMediaDevices.defaultAudioInput()
        self.ui.comboBox.addItem(
            default_device_info.description(), default_device_info
        )
        for device_info in self.m_devices.audioInputs():
            if device_info != default_device_info:
                self.ui.comboBox.addItem(device_info.description(), device_info)

        self.ui.comboBox.activated[int].connect(self.device_changed)
        self.ui.m_volume_slider.valueChanged.connect(self.m_slider_changed)
        self.initialize_mic(QMediaDevices.defaultAudioInput())

    def initialize_mic(self, device_info: QAudioDevice):
        format = QAudioFormat()
        format.setSampleRate(8000)
        format.setChannelCount(1)
        format.setSampleFormat(QAudioFormat.SampleFormat.Int16)

        self.m_audio_info = AudioInfo(format)

        self.m_audio_input = QAudioSource(device_info, format)
        initial_volume = QAudio.convertVolume(
            self.m_audio_input.volume(),
            QAudio.VolumeScale.LinearVolumeScale,
            QAudio.VolumeScale.LogarithmicVolumeScale,
        )
        self.ui.m_volume_slider.setValue(int(round(initial_volume * 100)))

        self.m_audio_input.stop()
        io = self.m_audio_input.start()

        def push_mode_slot():
            len = self.m_audio_input.bytesAvailable()
            buffer_size = 4096
            if len > buffer_size:
                len = buffer_size
            buffer: QByteArray = io.read(len)
            if len > 0:
                level = self.m_audio_info.calculate_level(buffer, len)
                self.m_canvas.set_level(level)

        io.readyRead.connect(push_mode_slot)

    @Slot(int)
    def device_changed(self, index):
        self.m_audio_input.stop()
        self.m_audio_input.disconnect(self)
        self.initialize_mic(self.ui.comboBox.itemData(index))

    @Slot(int)
    def output_device_changed(self, index):
        self.m_device = self.ui.comboBox_2.itemData(index)

    @Slot(int)
    def m_slider_changed(self, value):
        linearVolume = QAudio.convertVolume(value / float(100),
                                            QAudio.VolumeScale.LogarithmicVolumeScale,
                                            QAudio.VolumeScale.LinearVolumeScale)
        self.m_audio_input.setVolume(linearVolume)

    @Slot(int)
    def volume_changed(self, value):
        if self.m_audioSink is not None:
            self.m_audioSink.setVolume(value / 100.0)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("Audio Sources Example")
    input = AudioTest()
    input.show()
    sys.exit(app.exec())