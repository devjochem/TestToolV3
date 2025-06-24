# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'kbtest.ui'
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
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(993, 324)
        MainWindow.setMinimumSize(QSize(993, 324))
        MainWindow.setMaximumSize(QSize(993, 324))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 0, 991, 41))
        self.gridLayout = QGridLayout(self.horizontalLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.btnPRINT = QLabel(self.horizontalLayoutWidget)
        self.btnPRINT.setObjectName(u"btnPRINT")
        self.btnPRINT.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.btnPRINT, 0, 17, 1, 1)

        self.spacer3 = QLabel(self.horizontalLayoutWidget)
        self.spacer3.setObjectName(u"spacer3")

        self.gridLayout.addWidget(self.spacer3, 0, 1, 1, 1)

        self.btnF8 = QLabel(self.horizontalLayoutWidget)
        self.btnF8.setObjectName(u"btnF8")
        self.btnF8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.btnF8, 0, 10, 1, 1)

        self.btnF12 = QLabel(self.horizontalLayoutWidget)
        self.btnF12.setObjectName(u"btnF12")
        self.btnF12.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.btnF12, 0, 15, 1, 1)

        self.btnF2 = QLabel(self.horizontalLayoutWidget)
        self.btnF2.setObjectName(u"btnF2")
        self.btnF2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.btnF2, 0, 3, 1, 1)

        self.btnF6 = QLabel(self.horizontalLayoutWidget)
        self.btnF6.setObjectName(u"btnF6")
        self.btnF6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.btnF6, 0, 8, 1, 1)

        self.btnPAUSE = QLabel(self.horizontalLayoutWidget)
        self.btnPAUSE.setObjectName(u"btnPAUSE")
        self.btnPAUSE.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.btnPAUSE, 0, 19, 1, 1)

        self.spacer4 = QLabel(self.horizontalLayoutWidget)
        self.spacer4.setObjectName(u"spacer4")

        self.gridLayout.addWidget(self.spacer4, 0, 6, 1, 1)

        self.btnF5 = QLabel(self.horizontalLayoutWidget)
        self.btnF5.setObjectName(u"btnF5")
        self.btnF5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.btnF5, 0, 7, 1, 1)

        self.btnF4 = QLabel(self.horizontalLayoutWidget)
        self.btnF4.setObjectName(u"btnF4")
        self.btnF4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.btnF4, 0, 5, 1, 1)

        self.btnF1 = QLabel(self.horizontalLayoutWidget)
        self.btnF1.setObjectName(u"btnF1")
        self.btnF1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.btnF1, 0, 2, 1, 1)

        self.btnF7 = QLabel(self.horizontalLayoutWidget)
        self.btnF7.setObjectName(u"btnF7")
        self.btnF7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.btnF7, 0, 9, 1, 1)

        self.btnF9 = QLabel(self.horizontalLayoutWidget)
        self.btnF9.setObjectName(u"btnF9")
        self.btnF9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.btnF9, 0, 12, 1, 1)

        self.btnF3 = QLabel(self.horizontalLayoutWidget)
        self.btnF3.setObjectName(u"btnF3")
        self.btnF3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.btnF3, 0, 4, 1, 1)

        self.btnESCAPE = QLabel(self.horizontalLayoutWidget)
        self.btnESCAPE.setObjectName(u"btnESCAPE")
        self.btnESCAPE.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.btnESCAPE, 0, 0, 1, 1)

        self.btnF10 = QLabel(self.horizontalLayoutWidget)
        self.btnF10.setObjectName(u"btnF10")
        self.btnF10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.btnF10, 0, 13, 1, 1)

        self.btnSCROLL_LOCK = QLabel(self.horizontalLayoutWidget)
        self.btnSCROLL_LOCK.setObjectName(u"btnSCROLL_LOCK")
        self.btnSCROLL_LOCK.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.btnSCROLL_LOCK, 0, 18, 1, 1)

        self.spacer1 = QLabel(self.horizontalLayoutWidget)
        self.spacer1.setObjectName(u"spacer1")

        self.gridLayout.addWidget(self.spacer1, 0, 11, 1, 1)

        self.btnF11 = QLabel(self.horizontalLayoutWidget)
        self.btnF11.setObjectName(u"btnF11")
        self.btnF11.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.btnF11, 0, 14, 1, 1)

        self.spacer2 = QLabel(self.horizontalLayoutWidget)
        self.spacer2.setObjectName(u"spacer2")

        self.gridLayout.addWidget(self.spacer2, 0, 16, 1, 1)

        self.gridLayout.setColumnStretch(0, 10)
        self.gridLayout.setColumnStretch(1, 10)
        self.gridLayout.setColumnStretch(2, 10)
        self.gridLayout.setColumnStretch(3, 10)
        self.gridLayout.setColumnStretch(4, 10)
        self.gridLayout.setColumnStretch(5, 10)
        self.gridLayout.setColumnStretch(6, 5)
        self.gridLayout.setColumnStretch(7, 10)
        self.gridLayout.setColumnStretch(8, 10)
        self.gridLayout.setColumnStretch(9, 10)
        self.gridLayout.setColumnStretch(10, 10)
        self.gridLayout.setColumnStretch(11, 5)
        self.gridLayout.setColumnStretch(12, 10)
        self.gridLayout.setColumnStretch(13, 10)
        self.gridLayout.setColumnStretch(14, 10)
        self.gridLayout.setColumnStretch(15, 10)
        self.gridLayout.setColumnStretch(16, 2)
        self.gridLayout.setColumnStretch(17, 10)
        self.gridLayout.setColumnStretch(18, 10)
        self.gridLayout.setColumnStretch(19, 10)
        self.horizontalLayoutWidget_2 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(0, 50, 991, 51))
        self.gridLayout_2 = QGridLayout(self.horizontalLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btn1 = QLabel(self.horizontalLayoutWidget_2)
        self.btn1.setObjectName(u"btn1")
        self.btn1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.btn1, 0, 1, 1, 1)

        self.btn3 = QLabel(self.horizontalLayoutWidget_2)
        self.btn3.setObjectName(u"btn3")
        self.btn3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.btn3, 0, 3, 1, 1)

        self.btnEQUAL = QLabel(self.horizontalLayoutWidget_2)
        self.btnEQUAL.setObjectName(u"btnEQUAL")
        self.btnEQUAL.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.btnEQUAL, 0, 12, 1, 1)

        self.btn2 = QLabel(self.horizontalLayoutWidget_2)
        self.btn2.setObjectName(u"btn2")
        self.btn2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.btn2, 0, 2, 1, 1)

        self.btn7 = QLabel(self.horizontalLayoutWidget_2)
        self.btn7.setObjectName(u"btn7")
        self.btn7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.btn7, 0, 7, 1, 1)

        self.btnBACKSPACE = QLabel(self.horizontalLayoutWidget_2)
        self.btnBACKSPACE.setObjectName(u"btnBACKSPACE")
        self.btnBACKSPACE.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.btnBACKSPACE, 0, 13, 1, 1)

        self.btnGRAVE = QLabel(self.horizontalLayoutWidget_2)
        self.btnGRAVE.setObjectName(u"btnGRAVE")
        self.btnGRAVE.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.btnGRAVE, 0, 0, 1, 1)

        self.btnMINUS = QLabel(self.horizontalLayoutWidget_2)
        self.btnMINUS.setObjectName(u"btnMINUS")
        self.btnMINUS.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.btnMINUS, 0, 11, 1, 1)

        self.btn9 = QLabel(self.horizontalLayoutWidget_2)
        self.btn9.setObjectName(u"btn9")
        self.btn9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.btn9, 0, 9, 1, 1)

        self.btn4 = QLabel(self.horizontalLayoutWidget_2)
        self.btn4.setObjectName(u"btn4")
        self.btn4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.btn4, 0, 4, 1, 1)

        self.btnHOME = QLabel(self.horizontalLayoutWidget_2)
        self.btnHOME.setObjectName(u"btnHOME")
        self.btnHOME.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.btnHOME, 0, 16, 1, 1)

        self.btnPAGE_UP = QLabel(self.horizontalLayoutWidget_2)
        self.btnPAGE_UP.setObjectName(u"btnPAGE_UP")
        self.btnPAGE_UP.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.btnPAGE_UP, 0, 17, 1, 1)

        self.btnINSERT = QLabel(self.horizontalLayoutWidget_2)
        self.btnINSERT.setObjectName(u"btnINSERT")
        self.btnINSERT.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.btnINSERT, 0, 15, 1, 1)

        self.btn5 = QLabel(self.horizontalLayoutWidget_2)
        self.btn5.setObjectName(u"btn5")
        self.btn5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.btn5, 0, 5, 1, 1)

        self.btn6 = QLabel(self.horizontalLayoutWidget_2)
        self.btn6.setObjectName(u"btn6")
        self.btn6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.btn6, 0, 6, 1, 1)

        self.btn8 = QLabel(self.horizontalLayoutWidget_2)
        self.btn8.setObjectName(u"btn8")
        self.btn8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.btn8, 0, 8, 1, 1)

        self.btn0 = QLabel(self.horizontalLayoutWidget_2)
        self.btn0.setObjectName(u"btn0")
        self.btn0.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.btn0, 0, 10, 1, 1)

        self.spacer1_2 = QLabel(self.horizontalLayoutWidget_2)
        self.spacer1_2.setObjectName(u"spacer1_2")

        self.gridLayout_2.addWidget(self.spacer1_2, 0, 14, 1, 1)

        self.gridLayout_2.setColumnStretch(0, 10)
        self.gridLayout_2.setColumnStretch(1, 10)
        self.gridLayout_2.setColumnStretch(2, 10)
        self.gridLayout_2.setColumnStretch(3, 10)
        self.gridLayout_2.setColumnStretch(4, 10)
        self.gridLayout_2.setColumnStretch(5, 10)
        self.gridLayout_2.setColumnStretch(6, 10)
        self.gridLayout_2.setColumnStretch(7, 10)
        self.gridLayout_2.setColumnStretch(8, 10)
        self.gridLayout_2.setColumnStretch(9, 10)
        self.gridLayout_2.setColumnStretch(10, 10)
        self.gridLayout_2.setColumnStretch(11, 10)
        self.gridLayout_2.setColumnStretch(12, 10)
        self.gridLayout_2.setColumnStretch(13, 21)
        self.gridLayout_2.setColumnStretch(14, 2)
        self.gridLayout_2.setColumnStretch(15, 10)
        self.gridLayout_2.setColumnStretch(16, 10)
        self.gridLayout_2.setColumnStretch(17, 10)
        self.horizontalLayoutWidget_3 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(0, 100, 991, 51))
        self.gridLayout_3 = QGridLayout(self.horizontalLayoutWidget_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btnBRACKETLEFT = QLabel(self.horizontalLayoutWidget_3)
        self.btnBRACKETLEFT.setObjectName(u"btnBRACKETLEFT")
        self.btnBRACKETLEFT.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.btnBRACKETLEFT, 0, 11, 1, 1)

        self.btnE = QLabel(self.horizontalLayoutWidget_3)
        self.btnE.setObjectName(u"btnE")
        self.btnE.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.btnE, 0, 3, 1, 1)

        self.btnBRACKETRIGHT = QLabel(self.horizontalLayoutWidget_3)
        self.btnBRACKETRIGHT.setObjectName(u"btnBRACKETRIGHT")
        self.btnBRACKETRIGHT.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.btnBRACKETRIGHT, 0, 12, 1, 1)

        self.btnPAGE_DOWN = QLabel(self.horizontalLayoutWidget_3)
        self.btnPAGE_DOWN.setObjectName(u"btnPAGE_DOWN")
        self.btnPAGE_DOWN.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.btnPAGE_DOWN, 0, 17, 1, 1)

        self.btnQ = QLabel(self.horizontalLayoutWidget_3)
        self.btnQ.setObjectName(u"btnQ")
        self.btnQ.setEnabled(True)
        self.btnQ.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.btnQ, 0, 1, 1, 1)

        self.btnI = QLabel(self.horizontalLayoutWidget_3)
        self.btnI.setObjectName(u"btnI")
        self.btnI.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.btnI, 0, 8, 1, 1)

        self.btnY = QLabel(self.horizontalLayoutWidget_3)
        self.btnY.setObjectName(u"btnY")
        self.btnY.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.btnY, 0, 6, 1, 1)

        self.btnR = QLabel(self.horizontalLayoutWidget_3)
        self.btnR.setObjectName(u"btnR")
        self.btnR.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.btnR, 0, 4, 1, 1)

        self.btnP = QLabel(self.horizontalLayoutWidget_3)
        self.btnP.setObjectName(u"btnP")
        self.btnP.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.btnP, 0, 10, 1, 1)

        self.btnT = QLabel(self.horizontalLayoutWidget_3)
        self.btnT.setObjectName(u"btnT")
        self.btnT.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.btnT, 0, 5, 1, 1)

        self.btnDELETE = QLabel(self.horizontalLayoutWidget_3)
        self.btnDELETE.setObjectName(u"btnDELETE")
        self.btnDELETE.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.btnDELETE, 0, 15, 1, 1)

        self.btnTAB = QLabel(self.horizontalLayoutWidget_3)
        self.btnTAB.setObjectName(u"btnTAB")
        self.btnTAB.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.btnTAB, 0, 0, 1, 1)

        self.btnEND = QLabel(self.horizontalLayoutWidget_3)
        self.btnEND.setObjectName(u"btnEND")
        self.btnEND.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.btnEND, 0, 16, 1, 1)

        self.btnW = QLabel(self.horizontalLayoutWidget_3)
        self.btnW.setObjectName(u"btnW")
        self.btnW.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.btnW, 0, 2, 1, 1)

        self.btnO = QLabel(self.horizontalLayoutWidget_3)
        self.btnO.setObjectName(u"btnO")
        self.btnO.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.btnO, 0, 9, 1, 1)

        self.btnBACKSLASH = QLabel(self.horizontalLayoutWidget_3)
        self.btnBACKSLASH.setObjectName(u"btnBACKSLASH")
        self.btnBACKSLASH.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.btnBACKSLASH, 0, 13, 1, 1)

        self.btnU = QLabel(self.horizontalLayoutWidget_3)
        self.btnU.setObjectName(u"btnU")
        self.btnU.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.btnU, 0, 7, 1, 1)

        self.spacer1_3 = QLabel(self.horizontalLayoutWidget_3)
        self.spacer1_3.setObjectName(u"spacer1_3")

        self.gridLayout_3.addWidget(self.spacer1_3, 0, 14, 1, 1)

        self.gridLayout_3.setColumnStretch(0, 14)
        self.gridLayout_3.setColumnStretch(1, 10)
        self.gridLayout_3.setColumnStretch(2, 10)
        self.gridLayout_3.setColumnStretch(3, 10)
        self.gridLayout_3.setColumnStretch(4, 10)
        self.gridLayout_3.setColumnStretch(5, 10)
        self.gridLayout_3.setColumnStretch(6, 10)
        self.gridLayout_3.setColumnStretch(7, 10)
        self.gridLayout_3.setColumnStretch(8, 10)
        self.gridLayout_3.setColumnStretch(9, 10)
        self.gridLayout_3.setColumnStretch(10, 10)
        self.gridLayout_3.setColumnStretch(11, 10)
        self.gridLayout_3.setColumnStretch(12, 10)
        self.gridLayout_3.setColumnStretch(13, 17)
        self.gridLayout_3.setColumnStretch(14, 2)
        self.gridLayout_3.setColumnStretch(15, 10)
        self.gridLayout_3.setColumnStretch(16, 10)
        self.gridLayout_3.setColumnStretch(17, 10)
        self.horizontalLayoutWidget_4 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(0, 150, 991, 51))
        self.gridLayout_4 = QGridLayout(self.horizontalLayoutWidget_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btnK = QLabel(self.horizontalLayoutWidget_4)
        self.btnK.setObjectName(u"btnK")
        self.btnK.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.btnK, 0, 8, 1, 1)

        self.btnAPOSTROPHE = QLabel(self.horizontalLayoutWidget_4)
        self.btnAPOSTROPHE.setObjectName(u"btnAPOSTROPHE")
        self.btnAPOSTROPHE.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.btnAPOSTROPHE, 0, 11, 1, 1)

        self.btnS = QLabel(self.horizontalLayoutWidget_4)
        self.btnS.setObjectName(u"btnS")
        self.btnS.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.btnS, 0, 2, 1, 1)

        self.spacer2_2 = QLabel(self.horizontalLayoutWidget_4)
        self.spacer2_2.setObjectName(u"spacer2_2")
        self.spacer2_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.spacer2_2, 0, 14, 1, 1)

        self.btnA = QLabel(self.horizontalLayoutWidget_4)
        self.btnA.setObjectName(u"btnA")
        self.btnA.setEnabled(True)
        self.btnA.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.btnA, 0, 1, 1, 1)

        self.btnSEMICOLON = QLabel(self.horizontalLayoutWidget_4)
        self.btnSEMICOLON.setObjectName(u"btnSEMICOLON")
        self.btnSEMICOLON.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.btnSEMICOLON, 0, 10, 1, 1)

        self.btnG = QLabel(self.horizontalLayoutWidget_4)
        self.btnG.setObjectName(u"btnG")
        self.btnG.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.btnG, 0, 5, 1, 1)

        self.btnL = QLabel(self.horizontalLayoutWidget_4)
        self.btnL.setObjectName(u"btnL")
        self.btnL.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.btnL, 0, 9, 1, 1)

        self.btnF = QLabel(self.horizontalLayoutWidget_4)
        self.btnF.setObjectName(u"btnF")
        self.btnF.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.btnF, 0, 4, 1, 1)

        self.btnD = QLabel(self.horizontalLayoutWidget_4)
        self.btnD.setObjectName(u"btnD")
        self.btnD.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.btnD, 0, 3, 1, 1)

        self.spacer3_2 = QLabel(self.horizontalLayoutWidget_4)
        self.spacer3_2.setObjectName(u"spacer3_2")
        self.spacer3_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.spacer3_2, 0, 15, 1, 1)

        self.spacer4_2 = QLabel(self.horizontalLayoutWidget_4)
        self.spacer4_2.setObjectName(u"spacer4_2")

        self.gridLayout_4.addWidget(self.spacer4_2, 0, 16, 1, 1)

        self.btnH = QLabel(self.horizontalLayoutWidget_4)
        self.btnH.setObjectName(u"btnH")
        self.btnH.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.btnH, 0, 6, 1, 1)

        self.btnJ = QLabel(self.horizontalLayoutWidget_4)
        self.btnJ.setObjectName(u"btnJ")
        self.btnJ.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.btnJ, 0, 7, 1, 1)

        self.btnRETURN = QLabel(self.horizontalLayoutWidget_4)
        self.btnRETURN.setObjectName(u"btnRETURN")
        self.btnRETURN.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.btnRETURN, 0, 12, 1, 1)

        self.btnCAPS_LOCK = QLabel(self.horizontalLayoutWidget_4)
        self.btnCAPS_LOCK.setObjectName(u"btnCAPS_LOCK")
        self.btnCAPS_LOCK.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.btnCAPS_LOCK, 0, 0, 1, 1)

        self.spacer1_4 = QLabel(self.horizontalLayoutWidget_4)
        self.spacer1_4.setObjectName(u"spacer1_4")

        self.gridLayout_4.addWidget(self.spacer1_4, 0, 13, 1, 1)

        self.gridLayout_4.setColumnStretch(0, 20)
        self.gridLayout_4.setColumnStretch(1, 10)
        self.gridLayout_4.setColumnStretch(2, 10)
        self.gridLayout_4.setColumnStretch(3, 10)
        self.gridLayout_4.setColumnStretch(4, 10)
        self.gridLayout_4.setColumnStretch(5, 10)
        self.gridLayout_4.setColumnStretch(6, 10)
        self.gridLayout_4.setColumnStretch(7, 10)
        self.gridLayout_4.setColumnStretch(8, 10)
        self.gridLayout_4.setColumnStretch(9, 10)
        self.gridLayout_4.setColumnStretch(10, 10)
        self.gridLayout_4.setColumnStretch(11, 10)
        self.gridLayout_4.setColumnStretch(12, 22)
        self.gridLayout_4.setColumnStretch(13, 2)
        self.gridLayout_4.setColumnStretch(14, 10)
        self.gridLayout_4.setColumnStretch(15, 10)
        self.gridLayout_4.setColumnStretch(16, 10)
        self.horizontalLayoutWidget_5 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(0, 200, 991, 51))
        self.gridLayout_5 = QGridLayout(self.horizontalLayoutWidget_5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btnN = QLabel(self.horizontalLayoutWidget_5)
        self.btnN.setObjectName(u"btnN")
        self.btnN.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.btnN, 0, 6, 1, 1)

        self.spacer2_4 = QLabel(self.horizontalLayoutWidget_5)
        self.spacer2_4.setObjectName(u"spacer2_4")
        self.spacer2_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.spacer2_4, 0, 13, 1, 1)

        self.btnUP = QLabel(self.horizontalLayoutWidget_5)
        self.btnUP.setObjectName(u"btnUP")
        self.btnUP.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.btnUP, 0, 14, 1, 1)

        self.btnV = QLabel(self.horizontalLayoutWidget_5)
        self.btnV.setObjectName(u"btnV")
        self.btnV.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.btnV, 0, 4, 1, 1)

        self.btnCOMMA = QLabel(self.horizontalLayoutWidget_5)
        self.btnCOMMA.setObjectName(u"btnCOMMA")
        self.btnCOMMA.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.btnCOMMA, 0, 8, 1, 1)

        self.spacer1_5 = QLabel(self.horizontalLayoutWidget_5)
        self.spacer1_5.setObjectName(u"spacer1_5")

        self.gridLayout_5.addWidget(self.spacer1_5, 0, 15, 1, 1)

        self.btnSHIFT_L = QLabel(self.horizontalLayoutWidget_5)
        self.btnSHIFT_L.setObjectName(u"btnSHIFT_L")
        self.btnSHIFT_L.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.btnSHIFT_L, 0, 0, 1, 1)

        self.btnPERIOD = QLabel(self.horizontalLayoutWidget_5)
        self.btnPERIOD.setObjectName(u"btnPERIOD")
        self.btnPERIOD.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.btnPERIOD, 0, 9, 1, 1)

        self.btnX = QLabel(self.horizontalLayoutWidget_5)
        self.btnX.setObjectName(u"btnX")
        self.btnX.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.btnX, 0, 2, 1, 1)

        self.btnSHIFT_R = QLabel(self.horizontalLayoutWidget_5)
        self.btnSHIFT_R.setObjectName(u"btnSHIFT_R")
        self.btnSHIFT_R.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.btnSHIFT_R, 0, 11, 1, 1)

        self.btnSLASH = QLabel(self.horizontalLayoutWidget_5)
        self.btnSLASH.setObjectName(u"btnSLASH")
        self.btnSLASH.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.btnSLASH, 0, 10, 1, 1)

        self.btnC = QLabel(self.horizontalLayoutWidget_5)
        self.btnC.setObjectName(u"btnC")
        self.btnC.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.btnC, 0, 3, 1, 1)

        self.btnZ = QLabel(self.horizontalLayoutWidget_5)
        self.btnZ.setObjectName(u"btnZ")
        self.btnZ.setEnabled(True)
        self.btnZ.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.btnZ, 0, 1, 1, 1)

        self.btnB = QLabel(self.horizontalLayoutWidget_5)
        self.btnB.setObjectName(u"btnB")
        self.btnB.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.btnB, 0, 5, 1, 1)

        self.btnM = QLabel(self.horizontalLayoutWidget_5)
        self.btnM.setObjectName(u"btnM")
        self.btnM.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.btnM, 0, 7, 1, 1)

        self.spacer2_3 = QLabel(self.horizontalLayoutWidget_5)
        self.spacer2_3.setObjectName(u"spacer2_3")

        self.gridLayout_5.addWidget(self.spacer2_3, 0, 12, 1, 1)

        self.gridLayout_5.setColumnStretch(0, 26)
        self.gridLayout_5.setColumnStretch(1, 10)
        self.gridLayout_5.setColumnStretch(2, 10)
        self.gridLayout_5.setColumnStretch(3, 10)
        self.gridLayout_5.setColumnStretch(4, 10)
        self.gridLayout_5.setColumnStretch(5, 10)
        self.gridLayout_5.setColumnStretch(6, 10)
        self.gridLayout_5.setColumnStretch(7, 10)
        self.gridLayout_5.setColumnStretch(8, 10)
        self.gridLayout_5.setColumnStretch(9, 10)
        self.gridLayout_5.setColumnStretch(10, 10)
        self.gridLayout_5.setColumnStretch(11, 28)
        self.gridLayout_5.setColumnStretch(12, 2)
        self.gridLayout_5.setColumnStretch(13, 10)
        self.gridLayout_5.setColumnStretch(14, 10)
        self.gridLayout_5.setColumnStretch(15, 10)
        self.horizontalLayoutWidget_6 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_6.setObjectName(u"horizontalLayoutWidget_6")
        self.horizontalLayoutWidget_6.setGeometry(QRect(0, 250, 991, 51))
        self.gridLayout_6 = QGridLayout(self.horizontalLayoutWidget_6)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.btnDOWN = QLabel(self.horizontalLayoutWidget_6)
        self.btnDOWN.setObjectName(u"btnDOWN")
        self.btnDOWN.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_6.addWidget(self.btnDOWN, 0, 9, 1, 1)

        self.btnCONTROL_R = QLabel(self.horizontalLayoutWidget_6)
        self.btnCONTROL_R.setObjectName(u"btnCONTROL_R")
        self.btnCONTROL_R.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_6.addWidget(self.btnCONTROL_R, 0, 6, 1, 1)

        self.btnRIGHT = QLabel(self.horizontalLayoutWidget_6)
        self.btnRIGHT.setObjectName(u"btnRIGHT")
        self.btnRIGHT.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_6.addWidget(self.btnRIGHT, 0, 10, 1, 1)

        self.btnSPACE = QLabel(self.horizontalLayoutWidget_6)
        self.btnSPACE.setObjectName(u"btnSPACE")
        self.btnSPACE.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_6.addWidget(self.btnSPACE, 0, 3, 1, 1)

        self.btnALT_L = QLabel(self.horizontalLayoutWidget_6)
        self.btnALT_L.setObjectName(u"btnALT_L")
        self.btnALT_L.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_6.addWidget(self.btnALT_L, 0, 2, 1, 1)

        self.btnMENU = QLabel(self.horizontalLayoutWidget_6)
        self.btnMENU.setObjectName(u"btnMENU")
        self.btnMENU.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_6.addWidget(self.btnMENU, 0, 5, 1, 1)

        self.btnLEFT = QLabel(self.horizontalLayoutWidget_6)
        self.btnLEFT.setObjectName(u"btnLEFT")
        self.btnLEFT.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_6.addWidget(self.btnLEFT, 0, 8, 1, 1)

        self.btnALT_R = QLabel(self.horizontalLayoutWidget_6)
        self.btnALT_R.setObjectName(u"btnALT_R")
        self.btnALT_R.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_6.addWidget(self.btnALT_R, 0, 4, 1, 1)

        self.btnCONTROL_L = QLabel(self.horizontalLayoutWidget_6)
        self.btnCONTROL_L.setObjectName(u"btnCONTROL_L")
        self.btnCONTROL_L.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_6.addWidget(self.btnCONTROL_L, 0, 0, 1, 1)

        self.btnSUPER_L = QLabel(self.horizontalLayoutWidget_6)
        self.btnSUPER_L.setObjectName(u"btnSUPER_L")
        self.btnSUPER_L.setEnabled(True)
        self.btnSUPER_L.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_6.addWidget(self.btnSUPER_L, 0, 1, 1, 1)

        self.spacer1_6 = QLabel(self.horizontalLayoutWidget_6)
        self.spacer1_6.setObjectName(u"spacer1_6")

        self.gridLayout_6.addWidget(self.spacer1_6, 0, 7, 1, 1)

        self.gridLayout_6.setColumnStretch(0, 10)
        self.gridLayout_6.setColumnStretch(1, 10)
        self.gridLayout_6.setColumnStretch(2, 10)
        self.gridLayout_6.setColumnStretch(3, 100)
        self.gridLayout_6.setColumnStretch(4, 10)
        self.gridLayout_6.setColumnStretch(5, 10)
        self.gridLayout_6.setColumnStretch(6, 10)
        self.gridLayout_6.setColumnStretch(7, 2)
        self.gridLayout_6.setColumnStretch(8, 10)
        self.gridLayout_6.setColumnStretch(9, 10)
        self.gridLayout_6.setColumnStretch(10, 10)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Keyboard Tester", None))
        self.btnPRINT.setText(QCoreApplication.translate("MainWindow", u"PRTSC", None))
        self.spacer3.setText("")
        self.btnF8.setText(QCoreApplication.translate("MainWindow", u"F8", None))
        self.btnF12.setText(QCoreApplication.translate("MainWindow", u"F12", None))
        self.btnF2.setText(QCoreApplication.translate("MainWindow", u"F2", None))
        self.btnF6.setText(QCoreApplication.translate("MainWindow", u"F6", None))
        self.btnPAUSE.setText(QCoreApplication.translate("MainWindow", u"PAUSE", None))
        self.spacer4.setText("")
        self.btnF5.setText(QCoreApplication.translate("MainWindow", u"F5", None))
        self.btnF4.setText(QCoreApplication.translate("MainWindow", u"F4", None))
        self.btnF1.setText(QCoreApplication.translate("MainWindow", u"F1", None))
        self.btnF7.setText(QCoreApplication.translate("MainWindow", u"F7", None))
        self.btnF9.setText(QCoreApplication.translate("MainWindow", u"F9", None))
        self.btnF3.setText(QCoreApplication.translate("MainWindow", u"F3", None))
        self.btnESCAPE.setText(QCoreApplication.translate("MainWindow", u"ESC", None))
        self.btnF10.setText(QCoreApplication.translate("MainWindow", u"F10", None))
        self.btnSCROLL_LOCK.setText(QCoreApplication.translate("MainWindow", u"SCRLK", None))
        self.spacer1.setText("")
        self.btnF11.setText(QCoreApplication.translate("MainWindow", u"F11", None))
        self.spacer2.setText("")
        self.btn1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.btn3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.btnEQUAL.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.btn2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.btn7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.btnBACKSPACE.setText(QCoreApplication.translate("MainWindow", u"BCKSP", None))
        self.btnGRAVE.setText(QCoreApplication.translate("MainWindow", u"`", None))
        self.btnMINUS.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.btn9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.btn4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.btnHOME.setText(QCoreApplication.translate("MainWindow", u"HOME", None))
        self.btnPAGE_UP.setText(QCoreApplication.translate("MainWindow", u"PGUP", None))
        self.btnINSERT.setText(QCoreApplication.translate("MainWindow", u"INS", None))
        self.btn5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.btn6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.btn8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.btn0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.spacer1_2.setText("")
        self.btnBRACKETLEFT.setText(QCoreApplication.translate("MainWindow", u"[", None))
        self.btnE.setText(QCoreApplication.translate("MainWindow", u"E", None))
        self.btnBRACKETRIGHT.setText(QCoreApplication.translate("MainWindow", u"]", None))
        self.btnPAGE_DOWN.setText(QCoreApplication.translate("MainWindow", u"PGDW", None))
        self.btnQ.setText(QCoreApplication.translate("MainWindow", u"Q", None))
        self.btnI.setText(QCoreApplication.translate("MainWindow", u"I", None))
        self.btnY.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.btnR.setText(QCoreApplication.translate("MainWindow", u"R", None))
        self.btnP.setText(QCoreApplication.translate("MainWindow", u"P", None))
        self.btnT.setText(QCoreApplication.translate("MainWindow", u"T", None))
        self.btnDELETE.setText(QCoreApplication.translate("MainWindow", u"DEL", None))
        self.btnTAB.setText(QCoreApplication.translate("MainWindow", u"TAB", None))
        self.btnEND.setText(QCoreApplication.translate("MainWindow", u"END", None))
        self.btnW.setText(QCoreApplication.translate("MainWindow", u"W", None))
        self.btnO.setText(QCoreApplication.translate("MainWindow", u"O", None))
        self.btnBACKSLASH.setText(QCoreApplication.translate("MainWindow", u"\\", None))
        self.btnU.setText(QCoreApplication.translate("MainWindow", u"U", None))
        self.spacer1_3.setText("")
        self.btnK.setText(QCoreApplication.translate("MainWindow", u"K", None))
        self.btnAPOSTROPHE.setText(QCoreApplication.translate("MainWindow", u"'", None))
        self.btnS.setText(QCoreApplication.translate("MainWindow", u"S", None))
        self.spacer2_2.setText("")
        self.btnA.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.btnSEMICOLON.setText(QCoreApplication.translate("MainWindow", u";", None))
        self.btnG.setText(QCoreApplication.translate("MainWindow", u"G", None))
        self.btnL.setText(QCoreApplication.translate("MainWindow", u"L", None))
        self.btnF.setText(QCoreApplication.translate("MainWindow", u"F", None))
        self.btnD.setText(QCoreApplication.translate("MainWindow", u"D", None))
        self.spacer3_2.setText("")
        self.spacer4_2.setText("")
        self.btnH.setText(QCoreApplication.translate("MainWindow", u"H", None))
        self.btnJ.setText(QCoreApplication.translate("MainWindow", u"J", None))
        self.btnRETURN.setText(QCoreApplication.translate("MainWindow", u"ENTER", None))
        self.btnCAPS_LOCK.setText(QCoreApplication.translate("MainWindow", u"CAPS", None))
        self.spacer1_4.setText("")
        self.btnN.setText(QCoreApplication.translate("MainWindow", u"N", None))
        self.spacer2_4.setText("")
        self.btnUP.setText(QCoreApplication.translate("MainWindow", u"\u2191", None))
        self.btnV.setText(QCoreApplication.translate("MainWindow", u"V", None))
        self.btnCOMMA.setText(QCoreApplication.translate("MainWindow", u",", None))
        self.spacer1_5.setText("")
        self.btnSHIFT_L.setText(QCoreApplication.translate("MainWindow", u"SHIFT", None))
        self.btnPERIOD.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.btnX.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.btnSHIFT_R.setText(QCoreApplication.translate("MainWindow", u"SHIFT", None))
        self.btnSLASH.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.btnC.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.btnZ.setText(QCoreApplication.translate("MainWindow", u"Z", None))
        self.btnB.setText(QCoreApplication.translate("MainWindow", u"B", None))
        self.btnM.setText(QCoreApplication.translate("MainWindow", u"M", None))
        self.spacer2_3.setText("")
        self.btnDOWN.setText(QCoreApplication.translate("MainWindow", u"\u2193", None))
        self.btnCONTROL_R.setText(QCoreApplication.translate("MainWindow", u"CTRL", None))
        self.btnRIGHT.setText(QCoreApplication.translate("MainWindow", u"\u2192", None))
        self.btnSPACE.setText(QCoreApplication.translate("MainWindow", u"SPACE", None))
        self.btnALT_L.setText(QCoreApplication.translate("MainWindow", u"ALT", None))
        self.btnMENU.setText(QCoreApplication.translate("MainWindow", u"MENU", None))
        self.btnLEFT.setText(QCoreApplication.translate("MainWindow", u"\u2190", None))
        self.btnALT_R.setText(QCoreApplication.translate("MainWindow", u"ALT", None))
        self.btnCONTROL_L.setText(QCoreApplication.translate("MainWindow", u"CTRL", None))
        self.btnSUPER_L.setText(QCoreApplication.translate("MainWindow", u"WIN", None))
        self.spacer1_6.setText("")
    # retranslateUi

