import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import qtawesome
from modelanlysize import *
from help import *
from fault import *

class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_MainWindow,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(562, 404)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 20, 31, 31))
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(70, 20, 31, 31))
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(110, 20, 31, 31))
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.jump_help)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 90, 471, 51))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 160, 471, 51))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(230, 240, 101, 71))
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.jump_modelanlysize)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.close)
        self.pushButton_2.clicked.connect(MainWindow.lower)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "首页"))
        self.label.setText(_translate("MainWindow", "故障诊断分析工具"))
        self.label_2.setText(_translate("MainWindow", "点击按钮开始导入EFSM模型进行分析"))
        self.action.setText(_translate("MainWindow", "模型导入"))
        self.action_2.setText(_translate("MainWindow", "模型分析"))

        #窗口整体布局设计
        MainWindow.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        pe = QPalette()
        MainWindow.setAutoFillBackground(True)
        pe.setColor(QPalette.Window, Qt.lightGray)  # 设置背景色
        MainWindow.setPalette(pe)

        #左上角关闭最小化帮助按钮设计
        self.pushButton_2.setStyleSheet('''QPushButton{background:#F7D674;border-radius:15px;}
                        QPushButton:hover{background:yellow;}''')
        self.pushButton.setStyleSheet('''QPushButton{background:#F76677;border-radius:15px;}
                        QPushButton:hover{background:red;}''')
        spin_icon1 = qtawesome.icon('fa5s.question',color = 'white')
        self.pushButton_3.setIcon(spin_icon1)
        self.pushButton_3.setStyleSheet('''QPushButton{border-radius:15px;}
                        QPushButton:hover{color:white;
                            border:2px solid #F3F3F5;
                            background:darkGray;}''')

        #中间文字以及按钮风格设计
        self.label.setStyleSheet('''QLabel{color:white;font-size:30px;font-family:Roman times;}''')
        self.label_2.setStyleSheet('''QLabel{color:white;font-size:30px;font-family:Roman times;}''')
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label.setAlignment(Qt.AlignCenter)
        spin_icon2 = qtawesome.icon('fa5s.file-alt', color='white'  )
        self.pushButton_4.setIcon(spin_icon2)  # 设置图标
        self.pushButton_4.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_4.setStyleSheet('''QPushButton{border:none;}
                QPushButton:hover{color:white;
                            border:2px solid #F3F3F5;
                            border-radius:35px;
                            background:darkGray;}''')



    def jump_modelanlysize(self):
        dig = QFileDialog()
        dig.setFileMode(QFileDialog.ExistingFile)
        dig.setFilter(QDir.Files)
        if dig.exec_():
            filename = dig.selectedFiles()
            f = open(filename[0],'r',encoding='utf-8')
            with f:
                data = f.read()
        MainWindow.close()
        ui_form.show()
        ui_form.textBrowser_2.setText("")
        ui_form.textBrowser_2.setText(data)


    def jump_help(self):
        ui_help.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui_form = Ui_Form()
    ui_help = Ui_Form2()
    ui_fault = Ui_Form3()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())