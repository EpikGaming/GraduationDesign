from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette
import sys
import qtawesome

class Ui_Form2(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_Form2,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)

    def setupUi(self, Form2):
        Form2.setObjectName("Form2")
        Form2.resize(667, 350)
        self.label = QtWidgets.QLabel(Form2)
        self.label.setGeometry(QtCore.QRect(220, 0, 201, 71))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(Form2)
        self.textBrowser.setGeometry(QtCore.QRect(10, 80, 631, 221))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(Form2)
        self.pushButton.setGeometry(QtCore.QRect(20, 20, 31, 31))
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form2)
        self.pushButton_2.setGeometry(QtCore.QRect(60, 20, 31, 31))
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form2)
        self.pushButton.clicked.connect(Form2.close)
        self.pushButton_2.clicked.connect(Form2.lower)
        QtCore.QMetaObject.connectSlotsByName(Form2)

    def retranslateUi(self, Form2):
        _translate = QtCore.QCoreApplication.translate
        Form2.setWindowTitle(_translate("Form2", "帮助"))
        self.label.setText(_translate("Form2", "帮助"))
        self.textBrowser.setHtml(_translate("Form2", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
    "p, li { white-space: pre-wrap; }\n"
    "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">TXT内部格式说明：</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">T:(Ssrc,Stgt);event={};cond={};action={}</span></p>\n"
    "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">其中</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">T-迁移状态说明</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Ssrc-迁移的初始状态</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Stgt-迁移的结束状态</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">event-事件集说明</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">cond-条件集说明</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">action-动作集说明</span></p>\n"
    "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">example：</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">T1:(S1,S2);event={Initial-AB()};cond={};action={L1,L2=0m;V1,V2,V3=&quot;OFF&quot;;Q1,Q2,Q3=0}</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">T7:(S6,S3);event={If-L2};cond={L2&lt;=H2};action={Q1--}</span></p></body></html>"))

        Form2.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        pe = QPalette()
        Form2.setAutoFillBackground(True)
        pe.setColor(QPalette.Background, Qt.darkGray)
        Form2.setPalette(pe)

        self.pushButton.setStyleSheet('''QPushButton{background:#F76677;border-radius:15px;}
                        QPushButton:hover{background:red;}''')
        self.pushButton_2.setStyleSheet('''QPushButton{background:#F7D674;border-radius:15px;}
                        QPushButton:hover{background:yellow;}''')
        self.label.setStyleSheet('''QLabel{color:white;font-size:30px;font-family:Roman times;}''')
