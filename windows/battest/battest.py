# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'battest.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.batteriesInfo = QLineEdit(self.centralwidget)
        self.batteriesInfo.setObjectName(u"batteriesInfo")
        self.batteriesInfo.setDragEnabled(False)
        self.batteriesInfo.setReadOnly(True)

        self.gridLayout.addWidget(self.batteriesInfo, 0, 1, 1, 1)

        self.stopButton = QPushButton(self.centralwidget)
        self.stopButton.setObjectName(u"stopButton")

        self.gridLayout.addWidget(self.stopButton, 4, 0, 1, 1)

        self.healthInfo = QLineEdit(self.centralwidget)
        self.healthInfo.setObjectName(u"healthInfo")

        self.gridLayout.addWidget(self.healthInfo, 1, 1, 1, 1)

        self.startButton = QPushButton(self.centralwidget)
        self.startButton.setObjectName(u"startButton")

        self.gridLayout.addWidget(self.startButton, 3, 0, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.rateInfo = QLineEdit(self.centralwidget)
        self.rateInfo.setObjectName(u"rateInfo")

        self.gridLayout.addWidget(self.rateInfo, 2, 1, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout)

        self.graphLayout = QVBoxLayout()
        self.graphLayout.setObjectName(u"graphLayout")

        self.horizontalLayout.addLayout(self.graphLayout)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 640, 30))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.stopButton.setText(QCoreApplication.translate("MainWindow", u"End Test", None))
        self.startButton.setText(QCoreApplication.translate("MainWindow", u"Start Test", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Batteries found:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Health", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Rate", None))
        self.rateInfo.setText(QCoreApplication.translate("MainWindow", u"1000", None))
    # retranslateUi

