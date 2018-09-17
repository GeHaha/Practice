# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Calculator2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import sys

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def __init__(self):
        
         # 定义一个变量，确定是否按下运算符号,默认没有按下
        self.ispresign = False
        
        # 定义一个变量，储存输入的数字
        self.numlist = []
        
        # 定义一个记录是否按了等于号的变量
        self.isequalsign = 0
        
        # 定义一个变量记录是否按下了特殊符号的变量
        self.specialsign = 0
        
        
        
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(330, 418)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Button3 = QtWidgets.QPushButton(self.centralwidget)
        self.Button3.setGeometry(QtCore.QRect(130, 260, 51, 51))
        self.Button3.setStyleSheet("font: 75 14pt \"Arial\";")
        self.Button3.setObjectName("Button3")
        self.Button2 = QtWidgets.QPushButton(self.centralwidget)
        self.Button2.setGeometry(QtCore.QRect(70, 260, 51, 51))
        self.Button2.setStyleSheet("font: 75 14pt \"Arial\";")
        self.Button2.setObjectName("Button2")
        self.Button4 = QtWidgets.QPushButton(self.centralwidget)
        self.Button4.setGeometry(QtCore.QRect(10, 200, 51, 51))
        self.Button4.setStyleSheet("font: 75 14pt \"Arial\";")
        self.Button4.setObjectName("Button4")
        self.ButtonCE = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonCE.setGeometry(QtCore.QRect(250, 140, 51, 51))
        self.ButtonCE.setStyleSheet("font: 75 14pt \"Arial\";")
        self.ButtonCE.setObjectName("ButtonCE")
        self.ButtonChu = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonChu.setGeometry(QtCore.QRect(190, 140, 51, 51))
        self.ButtonChu.setStyleSheet("font: 75 14pt \"Arial\";")
        self.ButtonChu.setObjectName("ButtonChu")
        self.ButtonJian = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonJian.setGeometry(QtCore.QRect(190, 260, 51, 51))
        self.ButtonJian.setStyleSheet("font: 75 14pt \"Arial\";")
        self.ButtonJian.setObjectName("ButtonJian")
        self.ButtonDeng = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonDeng.setGeometry(QtCore.QRect(250, 260, 51, 111))
        self.ButtonDeng.setStyleSheet("font: 75 14pt \"Arial\";")
        self.ButtonDeng.setObjectName("ButtonDeng")
        self.Button8 = QtWidgets.QPushButton(self.centralwidget)
        self.Button8.setGeometry(QtCore.QRect(70, 140, 51, 51))
        self.Button8.setStyleSheet("font: 75 14pt \"Arial\";")
        self.Button8.setObjectName("Button8")
        self.ButtoncCheng = QtWidgets.QPushButton(self.centralwidget)
        self.ButtoncCheng.setGeometry(QtCore.QRect(190, 200, 51, 51))
        self.ButtoncCheng.setStyleSheet("font: 75 14pt \"Arial\";")
        self.ButtoncCheng.setObjectName("ButtoncCheng")
        self.Button7 = QtWidgets.QPushButton(self.centralwidget)
        self.Button7.setGeometry(QtCore.QRect(10, 140, 51, 51))
        self.Button7.setStyleSheet("font: 75 14pt \"Arial\";")
        self.Button7.setObjectName("Button7")
        self.Button0 = QtWidgets.QPushButton(self.centralwidget)
        self.Button0.setGeometry(QtCore.QRect(10, 320, 111, 51))
        self.Button0.setStyleSheet("font: 75 14pt \"Arial\";")
        self.Button0.setObjectName("Button0")
        self.Button9 = QtWidgets.QPushButton(self.centralwidget)
        self.Button9.setGeometry(QtCore.QRect(130, 140, 51, 51))
        self.Button9.setStyleSheet("font: 75 14pt \"Arial\";")
        self.Button9.setObjectName("Button9")
        self.Button1 = QtWidgets.QPushButton(self.centralwidget)
        self.Button1.setGeometry(QtCore.QRect(10, 260, 51, 51))
        self.Button1.setStyleSheet("font: 75 14pt \"Arial\";")
        self.Button1.setObjectName("Button1")
        self.ButtonDot = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonDot.setGeometry(QtCore.QRect(130, 320, 51, 51))
        self.ButtonDot.setStyleSheet("font: 75 14pt \"Arial\";")
        self.ButtonDot.setObjectName("ButtonDot")
        self.ButtonJia = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonJia.setGeometry(QtCore.QRect(190, 320, 51, 51))
        self.ButtonJia.setStyleSheet("font: 75 14pt \"Arial\";")
        self.ButtonJia.setObjectName("ButtonJia")
        self.Button6 = QtWidgets.QPushButton(self.centralwidget)
        self.Button6.setGeometry(QtCore.QRect(130, 200, 51, 51))
        self.Button6.setStyleSheet("font: 75 14pt \"Arial\";")
        self.Button6.setObjectName("Button6")
        self.ButtonDel = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonDel.setGeometry(QtCore.QRect(250, 200, 51, 51))
        self.ButtonDel.setStyleSheet("font: 75 14pt \"Arial\";")
        self.ButtonDel.setObjectName("ButtonDel")
        self.Button5 = QtWidgets.QPushButton(self.centralwidget)
        self.Button5.setGeometry(QtCore.QRect(70, 200, 51, 51))
        self.Button5.setStyleSheet("font: 75 14pt \"Arial\";")
        self.Button5.setObjectName("Button5")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 10, 291, 71))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(10, 80, 291, 51))
        self.textEdit_2.setObjectName("textEdit_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 330, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Mini计算器"))
        self.Button3.setText(_translate("MainWindow", "3"))
        self.Button3.clicked.connect(self.pressnum)
        
        self.Button2.setText(_translate("MainWindow", "2"))
        self.Button2.clicked.connect(self.pressnum)
        
        self.Button4.setText(_translate("MainWindow", "4"))
        self.Button4.clicked.connect(self.pressnum)
        
        self.ButtonCE.setText(_translate("MainWindow", "CE"))
        self.ButtonCE.clicked.connect(self.special)
        
        self.ButtonChu.setText(_translate("MainWindow", "÷"))
        self.ButtonChu.clicked.connect(self.presign)
        
        self.ButtonJian.setText(_translate("MainWindow", "-"))
        self.ButtonJian.clicked.connect(self.presign)
        
        self.ButtonDeng.setText(_translate("MainWindow", "="))
        self.ButtonDeng.clicked.connect(self.presseq)
        
        self.Button8.setText(_translate("MainWindow", "8"))
        self.Button8.clicked.connect(self.pressnum)
        
        self.ButtoncCheng.setText(_translate("MainWindow", "×"))
        self.ButtoncCheng.clicked.connect(self.presign)
        
        self.Button7.setText(_translate("MainWindow", "7"))
        self.Button7.clicked.connect(self.pressnum)
        
        self.Button0.setText(_translate("MainWindow", "0"))
        self.Button0.clicked.connect(self.pressnum)
        
        self.Button9.setText(_translate("MainWindow", "9"))
        self.Button9.clicked.connect(self.pressnum)
        
        self.Button1.setText(_translate("MainWindow", "1"))
        self.Button1.clicked.connect(self.pressnum)
        
        self.ButtonDot.setText(_translate("MainWindow", "."))
        self.ButtonDot.clicked.connect(self.pressnum)
        
        self.ButtonJia.setText(_translate("MainWindow", "+"))
        self.ButtonJia.clicked.connect(self.pressnum
        
        self.Button6.setText(_translate("MainWindow", "6"))
        self.Button6.clicked.connect(self.pressnum)
        
        self.ButtonDel.setText(_translate("MainWindow", "Del"))
        self.ButtonDel.clicked.connect(self.special)
        
        self.Button5.setText(_translate("MainWindow", "5"))
        self.Button5.clicked.connect(self.pressnum)
        
    """
        # 按下数字的函数
    def pressnum(self,num):
        
        # 判断是否按下了运算符号
        if self.ispresign == True:
            # 如果按下了符号，将面板数字重置为 0
            self.value1.set('0')
            # 将按下运算符号的标志重置
            self.ispresign = False
            
        # 判断是否按下了等于号
        if self.isequalsign == 1:
            self.value1.set('0')
            self.isequalsign = 0
            
        #判断是否按下了特殊符号    
        if self.specialsign == 1:
            self.value1.set('0')
            self.specialsign = 0
            
        # 获得面板上的数字
        oldnum = self.value1.get()
        
        # 判断面板上的是否为指定的数据
        if oldnum == '除数不能为0':
            return
        else:
            # 判断按下的(.)点是否在已有数据中
            if num == '.' and num in oldnum:
                res = oldnum
                
            # 判断按下点的时候原有数据是否为0
            elif num == '.' and oldnum == '0':
                res = oldnum + '.'
                
            # 如果面板上的数字是0，则把第一个数字储存起来
            elif oldnum == '0':
                res = num
                
            # 如果不是0，则和之前的数字链接起来，给变量self.value1
            else:
                res = oldnum + num
            self.value1.set(res)

    # 按下运算符号的函数()
    def presign(self,sign):
        # 判断之前是否已经按过运算符号
        if self.ispresign == True and self.numlist != []:  # True  表示上一次按过运算符号
            self.numlist[-1] = sign  # 把第二次按的运算符号替换成上次的运算符号
        else:
            # 获得面板上的数字
            oldnum = self.value1.get()
            if oldnum == '除数不能为0':
                self.value1.set('除数不能为0')
            else:
                # 先将面板上的数字储存到列表中
                self.numlist.append(oldnum)
                # 再将按下的符号储存到列表
                self.numlist.append(sign)
        # 按下符号，会将按下符号标志的状态记录下来
        self.ispresign = True

    # 按下特殊符号的按钮（C清空所有，CE清空当前，消除最后一位）
    def special(self,sign):
        
        # 获得当前面板上的内容
        strs = self.value1.get()
        
        if sign == 'CE':
            # 直接清空列表
            self.numlist.clear()
            
            self.value2.set('')
            # 将面板上的置为0
            res = 0
        elif sign == '←':
            if strs != '除数不能为0':
                # 判断面板上数字是否为0
                if strs != '0':
                    # 判断面板上数字是否就一位数
                    if len(strs) != 1:
                        # 进行切片操作
                        res = strs[0:-1]
                    else:
                        # 如果就一位数字直接变为0
                        res = '0'
                    if self.isequalsign == 1:
                        res = strs
                else:
                    # 若等于0 则不进行操作
                    res = '0'
            else:
                res = strs

        # 将是否按下特殊符号的标志置为已按（用1表示）
        self.specialsign = 1
        # 将上面处理的数字放到面板中
        self.value1.set(res)

    # 计算结果
    def presseq(self,signeq):
        
        # 获得面板上数字
        oldnum = self.value1.get()
        if self.isequalsign == 1:
            self.value1.set(oldnum)
            self.isequalsign = 0
            
        elif self.specialsign == 1:
            self.value1.set(oldnum)
            self.specialsign = 0
            
        elif self.numlist == []:
            self.value1.set(oldnum)
            
        else:
            if oldnum == '除数不能为0':
                self.value1.set(oldnum)
            else:
                # 判断进行除法操作的时候，除数是否为0
                if self.numlist[-1] == '/' and eval(oldnum) == 0:
                    self.value1.set('除数不能为0')
                    self.numlist.clear()
                else:
                    # 将获得的数字添加到列表中
                    self.numlist.append(oldnum)
                    # 将列表中的字符串连接成字符串
                    result = ''.join(self.numlist)
                    # 将连接的字符串进行运算
                    self.value1.set(eval(result)) 
                    #将运算过程显示到屏幕2
                    self.value2.set(result)
                    
                    # 清空列表
                    self.numlist.clear()
        # 将是否按下等号的标志设置为已按（用1表示）
        self.isequalsign = 1
    """

#调用程序    
if __name__ == '__main__':
    
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)     
    MainWindow.show() 
    sys.exit(app.exec_()) 
