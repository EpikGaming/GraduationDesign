import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import qtawesome
from modelanlysize import *
from help import *
from mainui import *
from CondDeal import *
from EventDeal import *
from ActionDeal import *
from MakeGraph import *
from DataDependence import *
from FindPath import *
from DDGraph import *
import networkx as nx
import matplotlib.pyplot as plt

class Ui_Form3(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_Form3,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)

    def setupUi(self, Form3):
        Form3.setObjectName("Form")
        Form3.resize(550, 310)
        self.comboBox = QtWidgets.QComboBox(Form3)
        self.comboBox.setGeometry(QtCore.QRect(30, 170, 101, 41))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.textBrowser = QtWidgets.QTextBrowser(Form3)
        self.textBrowser.setGeometry(QtCore.QRect(320, 30, 211, 251))
        self.textBrowser.setObjectName("textBrowser")
        self.comboBox_2 = QtWidgets.QComboBox(Form3)
        self.comboBox_2.setGeometry(QtCore.QRect(160, 170, 101, 41))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.pushButton = QtWidgets.QPushButton(Form3)
        self.pushButton.setGeometry(QtCore.QRect(30, 10, 31, 31))
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form3)
        self.pushButton_2.setGeometry(QtCore.QRect(80, 10, 31, 31))
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_4 = QtWidgets.QPushButton(Form3)
        self.pushButton_4.setGeometry(QtCore.QRect(70, 230, 151, 51))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.analyse)  #数据依赖图分析
        self.label = QtWidgets.QLabel(Form3)
        self.label.setGeometry(QtCore.QRect(10, 70, 281, 61))
        self.label.setText("")
        self.label.setObjectName("label")
        self.textBrowser_2 = QtWidgets.QTextBrowser(Form3)
        self.textBrowser_2.setGeometry(QtCore.QRect(550, 280, 20, 20))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_3 = QtWidgets.QTextBrowser(Form3)
        self.textBrowser_3.setGeometry(QtCore.QRect(580, 280, 20, 20))
        self.textBrowser_3.setObjectName("textBrowser_3")

        self.retranslateUi(Form3)
        self.pushButton.clicked.connect(Form3.close)
        self.pushButton_2.clicked.connect(Form3.lower)
        QtCore.QMetaObject.connectSlotsByName(Form3)


    def retranslateUi(self, Form3):
        _translate = QtCore.QCoreApplication.translate
        Form3.setWindowTitle(_translate("Form", "Form"))
        self.comboBox.setItemText(0, _translate("Form", "选择故障源"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.comboBox_2.setItemText(0, _translate("Form", "选择正负偏差"))
        self.comboBox_2.setItemText(1, _translate("Form", "正/+"))
        self.comboBox_2.setItemText(2, _translate("Form", "负/-"))
        self.pushButton_4.setText(_translate("Form", "故障原因分析"))


        # 窗口整体布局设计
        Form3.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        pe = QPalette()
        Form3.setAutoFillBackground(True)
        pe.setColor(QPalette.Window, Qt.lightGray)
        Form3.setPalette(pe)

        # 左上角关闭最小化按钮设计
        self.pushButton.setStyleSheet('''QPushButton{background:#F76677;border-radius:15px;}QPushButton:hover{background:red;}''')
        self.pushButton_2.setStyleSheet('''QPushButton{background:#F7D674;border-radius:15px;}QPushButton:hover{background:yellow;}''')

        self.textBrowser.setStyleSheet('''QLabel{color:black;font-size:15px;font-family:Roman times;}''')

    def analyse(self):
        txt1 = self.comboBox.currentText()
        txt2 = self.comboBox_2.currentText()
        self.textBrowser.setText("")
        if txt1 != "选择故障源" and txt2 != "选择正负偏差":
            # print(txt1)
            if txt2 == "正/+":
                txt = "造成变量" + str(txt1) + "过大/偏大的原因有：" + "\n"
                txt += "(1)变量" + txt1 + "所处容器故障" + "\n"
                DDlist = MakeDDList(txt1,[])
                txt += DisplayTxT(DDlist,txt1)
                DDlist = []
            # print(DDlist)
                self.textBrowser.setText(txt)
                self.textBrowser.setStyleSheet('''QLabel{color:black;font-size:15px;font-family:Roman times;}''')
                DrawDDGragh(DDlist,txt)
            elif txt2 == "负/-":
                txt = "造成变量" + str(txt1) + "过大/偏大的原因有：" + "\n"      #还是偏大，因为后续会将字符大与字符小相互调换
                txt += "(1)变量" + txt1 + "所处容器故障" + "\n"
                DDlist = MakeDDList(txt1, [])
                txt += DisplayTxT(DDlist, txt1)
                DDlist = []
                # print(DDlist)
                txt = re.sub("大","。",txt)
                txt = re.sub("小", "大", txt)
                txt = re.sub("。", "小", txt)
                self.textBrowser.setText(txt)
                self.textBrowser.setStyleSheet('''QLabel{color:black;font-size:15px;font-family:Roman times;}''')
                DrawDDGragh(DDlist, txt)
        else:
            self.textBrowser.setText("请选择故障源以及正负关系进行分析")