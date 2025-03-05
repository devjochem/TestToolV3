# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHeaderView, QLayout,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTableWidget, QTableWidgetItem, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1197, 699)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SizeConstraint.SetMinAndMaxSize)
        self.pushButton_kb = QPushButton(self.centralwidget)
        self.pushButton_kb.setObjectName(u"pushButton_kb")

        self.verticalLayout.addWidget(self.pushButton_kb)

        self.pushButton_cm = QPushButton(self.centralwidget)
        self.pushButton_cm.setObjectName(u"pushButton_cm")

        self.verticalLayout.addWidget(self.pushButton_cm)

        self.pushButton_lcd = QPushButton(self.centralwidget)
        self.pushButton_lcd.setObjectName(u"pushButton_lcd")

        self.verticalLayout.addWidget(self.pushButton_lcd)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout.addWidget(self.pushButton_2)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 2, 1)

        self.userOutput = QTextEdit(self.centralwidget)
        self.userOutput.setObjectName(u"userOutput")
        self.userOutput.setReadOnly(True)

        self.gridLayout.addWidget(self.userOutput, 0, 1, 1, 1)

        self.batteryTable = QTableWidget(self.centralwidget)
        self.batteryTable.setObjectName(u"batteryTable")

        self.gridLayout.addWidget(self.batteryTable, 1, 1, 1, 2)

        self.diskTable = QTableWidget(self.centralwidget)
        self.diskTable.setObjectName(u"diskTable")

        self.gridLayout.addWidget(self.diskTable, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1197, 30))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_kb.setText(QCoreApplication.translate("MainWindow", u"Keyboard", None))
        self.pushButton_cm.setText(QCoreApplication.translate("MainWindow", u"Camera", None))
        self.pushButton_lcd.setText(QCoreApplication.translate("MainWindow", u"LCD", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Sound", None))
        self.userOutput.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Noto Sans'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
    # retranslateUi

