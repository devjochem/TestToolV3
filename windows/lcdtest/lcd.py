# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'lcd.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QWidget)

class Ui_LCDTest(object):
    def setupUi(self, LCDTest):
        if not LCDTest.objectName():
            LCDTest.setObjectName(u"LCDTest")
        LCDTest.resize(640, 480)
        self.centralwidget = QWidget(LCDTest)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 3, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 0, 1, 1, 1)

        #self.exitButton = QPushButton(self.centralwidget)
        #self.exitButton.setObjectName(u"exitButton")
        #self.exitButton.setAutoDefault(False)

        #self.gridLayout.addWidget(self.exitButton, 1, 1, 1, 1)

        LCDTest.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(LCDTest)
        self.statusbar.setObjectName(u"statusbar")
        LCDTest.setStatusBar(self.statusbar)

        self.retranslateUi(LCDTest)

        QMetaObject.connectSlotsByName(LCDTest)
    # setupUi

    def retranslateUi(self, LCDTest):
        LCDTest.setWindowTitle(QCoreApplication.translate("LCDTest", u"MainWindow", None))
        #self.exitButton.setText(QCoreApplication.translate("LCDTest", u"Exit", None))
    # retranslateUi

