# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'camtest.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btnCam0 = QPushButton(self.centralwidget)
        self.btnCam0.setObjectName(u"btnCam0")
        self.btnCam0.setEnabled(False)

        self.verticalLayout.addWidget(self.btnCam0)

        self.btnCam1 = QPushButton(self.centralwidget)
        self.btnCam1.setObjectName(u"btnCam1")
        self.btnCam1.setEnabled(False)

        self.verticalLayout.addWidget(self.btnCam1)

        self.btnCam2 = QPushButton(self.centralwidget)
        self.btnCam2.setObjectName(u"btnCam2")
        self.btnCam2.setEnabled(False)

        self.verticalLayout.addWidget(self.btnCam2)

        self.btnCam3 = QPushButton(self.centralwidget)
        self.btnCam3.setObjectName(u"btnCam3")
        self.btnCam3.setEnabled(False)

        self.verticalLayout.addWidget(self.btnCam3)

        self.btnCam4 = QPushButton(self.centralwidget)
        self.btnCam4.setObjectName(u"btnCam4")
        self.btnCam4.setEnabled(False)

        self.verticalLayout.addWidget(self.btnCam4)


        self.gridLayout_2.addLayout(self.verticalLayout, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Camera Test", None))
        self.label.setText("")
        self.btnCam0.setText(QCoreApplication.translate("MainWindow", u"Camera 1", None))
        self.btnCam1.setText(QCoreApplication.translate("MainWindow", u"Camera 2", None))
        self.btnCam2.setText(QCoreApplication.translate("MainWindow", u"Camera 3", None))
        self.btnCam3.setText(QCoreApplication.translate("MainWindow", u"Camera 4", None))
        self.btnCam4.setText(QCoreApplication.translate("MainWindow", u"Camera 5", None))
    # retranslateUi

