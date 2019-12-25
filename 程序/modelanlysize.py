import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import qtawesome
from modelanlysize import *
from help import *
from mainui import *
from help import *
from fault import *
from CondDeal import *
from EventDeal import *
from ActionDeal import *
from MakeGraph import *
from DataDependence import *
import networkx as nx
import matplotlib.pyplot as plt

class Ui_Form(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_Form,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(746, 668)
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(460, 170, 281, 411))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton_1 = QtWidgets.QPushButton(Form)
        self.pushButton_1.setGeometry(QtCore.QRect(10, 10, 31, 31))
        self.pushButton_1.setText("")
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 10, 31, 31))
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 150, 160, 431))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_4 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout.addWidget(self.pushButton_5)
        self.pushButton_5.clicked.connect(self.jump_Graph)#状态转移图分析
        self.pushButton_6 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.jump_Event)#事件集分析
        self.verticalLayout.addWidget(self.pushButton_6)
        self.pushButton_7 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(self.jump_Condition)#条件集分析
        self.verticalLayout.addWidget(self.pushButton_7)
        self.pushButton_8 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.clicked.connect(self.jump_Action)#动作集分析
        self.verticalLayout.addWidget(self.pushButton_8)
        self.pushButton_9 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_9.clicked.connect(self.jump_DataDependence)#数据依赖关系分析
        self.verticalLayout.addWidget(self.pushButton_9)
        self.textBrowser_2 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_2.setGeometry(QtCore.QRect(160, 170, 261, 411))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(540, 10, 71, 61))
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.jump_Mainui)#跳转到首页
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(630, 10, 71, 61))
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.jump_Analysis)#跳转到故障诊断
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(190, 120, 201, 41))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(500, 120, 201, 41))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(540, 70, 71, 31))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(630, 70, 71, 31))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.pushButton_4.clicked.connect(self.jump_Matrixs)#邻接矩阵分析

        self.retranslateUi(Form)
        self.pushButton_1.clicked.connect(Form.close)
        self.pushButton_2.clicked.connect(Form.lower)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_4.setText(_translate("Form", "邻接矩阵"))
        self.pushButton_5.setText(_translate("Form", "状态转移图"))
        self.pushButton_6.setText(_translate("Form", "事件集"))
        self.pushButton_7.setText(_translate("Form", "条件集"))
        self.pushButton_8.setText(_translate("Form", "动作集"))
        self.pushButton_9.setText(_translate("Form", "数据依赖关系"))
        self.label.setText(_translate("Form", "EFSM模型描述"))
        self.label_2.setText(_translate("Form", "内部具体描述"))
        self.label_3.setText(_translate("Form", "首页"))
        self.label_4.setText(_translate("Form", "故障诊断"))

        #窗口整体布局设计
        Form.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        pe = QPalette()
        Form.setAutoFillBackground(True)
        pe.setColor(QPalette.Window,Qt.lightGray)
        Form.setPalette(pe)

        #左上角关闭最小化按钮设计
        self.pushButton_1.setStyleSheet('''QPushButton{background:#F76677;border-radius:15px;}
                        QPushButton:hover{background:red;}''')
        self.pushButton_2.setStyleSheet('''QPushButton{background:#F7D674;border-radius:15px;}
                        QPushButton:hover{background:yellow;}''')

        #右上角工具按钮设计
        spin_icon1 = qtawesome.icon('fa5s.home',color = 'white')
        self.pushButton.setIcon(spin_icon1)
        self.pushButton.setIconSize(QtCore.QSize(40, 40))
        self.pushButton.setStyleSheet('''QPushButton{border-radius:30px;}
                                QPushButton:hover{color:white;
                                    border:2px solid #F3F3F5;
                                    background:darkGray;}''')
        spin_icon2 = qtawesome.icon('fa5s.wrench',color = 'white')
        self.pushButton_3.setIcon(spin_icon2)
        self.pushButton_3.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_3.setStyleSheet('''QPushButton{border-radius:30px;}
                                QPushButton:hover{color:white;
                                    border:2px solid #F3F3F5;
                                    background:darkGray;}''')

        #右上角文字设计
        self.label_3.setStyleSheet('''QLabel{color:white;font-size:15px;font-family:Roman times;}''')
        self.label_4.setStyleSheet('''QLabel{color:white;font-size:15px;font-family:Roman times;}''')

        #textBrowser描述文字设计
        self.label.setStyleSheet('''QLabel{color:black;font-size:25px;font-family:Roman times;}''')
        self.label_2.setStyleSheet('''QLabel{color:black;font-size:25px;font-family:Roman times;}''')


    def jump_Mainui(self):
        self.close()
        self.Main = Ui_MainWindow()
        self.Main.show()

    def jump_Analysis(self):
        self.fault = Ui_Form3()
        self.fault.show()
        _translate = QtCore.QCoreApplication.translate
        with open('EFSM.txt')as file_object:
            contents = file_object.read()  # 读取迁移内变量集
        T = ['T0', 'T1', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'T8', 'T9', 'T10', 'T11', 'T12', 'T13', 'T14', 'T15',
             'T16', 'T17', 'T18', 'T19', 'T20']
        X = modifylist(contents, T)
        act = ActionDeal(contents, X)
        S = MakeState(contents, X)
        matrixS = MakeMatrix(contents, X)
        DD = MakeDataDependence(act, X)
        fault = FindFault(DD)
        txt = FindFaultDisplay(DD)
        faultvariable = []
        self.fault.label.setText("")
        self.fault.label.setText(txt)
        txt2 = ""
        for value in fault.values():
            txt2 += str(value) + ","
        txt2 = txt2[:-1]            #删去最后一个符号
        items = txt2.split(",")
        for item in items:
            self.fault.comboBox.addItem("")
        for j in range(1,len(items)+1):
            self.fault.comboBox.setItemText(j, _translate("Form", items[j-1]))

    def jump_Matrixs(self):
        self.textBrowser.setText("")    #初始化
        contents = self.textBrowser_2.toPlainText()
        T = ['T0', 'T1', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'T8', 'T9', 'T10', 'T11', 'T12', 'T13', 'T14', 'T15',
             'T16', 'T17', 'T18', 'T19', 'T20']
        X = modifylist(contents, T)
        txt = MakeMatrixDisplay(contents,X)
        #txt += "\n" + MakeMatrixDisplay2(contents,X)
        self.textBrowser.setText(txt)

    def jump_Graph(self):
        self.textBrowser.setText("")    #初始化
        contents = self.textBrowser_2.toPlainText()
        T = ['T0', 'T1', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'T8', 'T9', 'T10', 'T11', 'T12', 'T13', 'T14', 'T15',
             'T16', 'T17', 'T18', 'T19', 'T20']
        X = modifylist(contents, T)
        S = MakeState(contents,X)           #取得状态集
        matrixS = MakeMatrix(contents,X)    #取得邻接矩阵
        DrawPicture(matrixS,S)

    def jump_Event(self):
        self.textBrowser.setText("")    #初始化
        contents = self.textBrowser_2.toPlainText()
        T = ['T0', 'T1', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'T8', 'T9', 'T10', 'T11', 'T12', 'T13', 'T14', 'T15',
             'T16', 'T17', 'T18', 'T19', 'T20']
        X = modifylist(contents, T)
        txt = EventDeal(contents,X)
        self.textBrowser.setText(txt)

    def jump_Condition(self):
        self.textBrowser.setText("")    #初始化
        contents = self.textBrowser_2.toPlainText()
        T = ['T0', 'T1', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'T8', 'T9', 'T10', 'T11', 'T12', 'T13', 'T14', 'T15',
             'T16', 'T17', 'T18', 'T19', 'T20']
        X = modifylist(contents, T)
        txt = ConditionDeal(contents,X)
        self.textBrowser.setText(txt)

    def jump_Action(self):
        self.textBrowser.setText("")    #初始化
        contents = self.textBrowser_2.toPlainText()
        T = ['T0', 'T1', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'T8', 'T9', 'T10', 'T11', 'T12', 'T13', 'T14', 'T15',
             'T16', 'T17', 'T18', 'T19', 'T20']
        X = modifylist(contents, T)
        txt = ActionDealDisplay(contents,X)
        self.textBrowser.setText(txt)

    def jump_DataDependence(self):
        self.textBrowser.setText("")    #初始化
        contents = self.textBrowser_2.toPlainText()
        T = ['T0', 'T1', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'T8', 'T9', 'T10', 'T11', 'T12', 'T13', 'T14', 'T15',
             'T16', 'T17', 'T18', 'T19', 'T20']
        X = modifylist(contents, T)
        act = ActionDeal(contents,X)
        txt = DataDependenceDisplay(act,X)
        self.textBrowser.setText(txt)

