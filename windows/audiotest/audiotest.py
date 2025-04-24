# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'audiotest.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSlider,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(614, 219)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.comboBox_2 = QComboBox(self.centralwidget)
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.gridLayout_3.addWidget(self.comboBox_2, 0, 1, 1, 1)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_3.addWidget(self.label_3, 1, 0, 1, 1)

        self.ma_volume_slider = QSlider(self.centralwidget)
        self.ma_volume_slider.setObjectName(u"ma_volume_slider")
        self.ma_volume_slider.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_3.addWidget(self.ma_volume_slider, 1, 1, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_3, 0, 1, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout_2.addWidget(self.comboBox, 0, 1, 1, 1)

        self.m_volume_slider = QSlider(self.centralwidget)
        self.m_volume_slider.setObjectName(u"m_volume_slider")
        self.m_volume_slider.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_2.addWidget(self.m_volume_slider, 1, 0, 1, 2)


        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        self.micLevels = QGridLayout()
        self.micLevels.setObjectName(u"micLevels")

        self.gridLayout.addLayout(self.micLevels, 1, 0, 1, 1)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_5.addWidget(self.pushButton, 0, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout_5.addWidget(self.pushButton_2, 0, 1, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_5, 1, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"AudioTest", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Master:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Speaker", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Microphone", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Test Left", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Test Right", None))
    # retranslateUi

