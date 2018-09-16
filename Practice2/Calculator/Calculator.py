# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Calculator.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import re
#from PyQt.QtWidgets import QApplication ,QWidget,QPushButton,QVBoxLayout, QGridLayout, QGroupBox, QLineEdit
import sys
from PyQt5.QtCore import Qt


class Ui_MainWindow(QtGui.QWidgets):
    def __init__(self,parent = None):
        QtGui.QWidegt.__init__(self,parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Mini计算器")
        MainWindow.resize(324, 430)
        
        self.resultflag = 0
        self.errflag = 0
        
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
        
        #显示区   
        self.display = QtWidgets.QTextEdit(self.centralwidget)
        self.display.setGeometry(QtCore.QRect(10, 10, 291, 121))
        self.display.setObjectName("textEdit")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 324, 23))
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
        self.Button3.clicked.connect(self.on_click)
        
        self.Button2.setText(_translate("MainWindow", "2"))
        self.Button2.clicked.connect(self.on_click)
        
        self.Button4.setText(_translate("MainWindow", "4"))
        self.Button4.clicked.connect(self.on_click)
        
        self.ButtonCE.setText(_translate("MainWindow", "CE"))
        self.ButtonCE.clicked.connect(self.on_click)
        
        self.ButtonChu.setText(_translate("MainWindow", "÷"))
        self.ButtonChu.clicked.connect(self.on_click)
        
        self.ButtonJian.setText(_translate("MainWindow", "-"))
        self.ButtonJian.clicked.connect(self.on_click)
        
        self.ButtonDeng.setText(_translate("MainWindow", "="))
        self.ButtonDeng.clicked.connect(self.on_click)
        
        self.Button8.setText(_translate("MainWindow", "8"))
        self.Button8.clicked.connect(self.on_click)
        
        self.ButtoncCheng.setText(_translate("MainWindow", "×"))
        self.ButtoncCheng.clicked.connect(self.on_click)
        
        self.Button7.setText(_translate("MainWindow", "7"))
        self.Button7.clicked.connect(self.on_click)
        
        self.Button0.setText(_translate("MainWindow", "0"))
        self.Button0.clicked.connect(self.on_click)
        
        self.Button9.setText(_translate("MainWindow", "9"))
        self.Button9.clicked.connect(self.on_click)
        
        self.Button1.setText(_translate("MainWindow", "1"))
        self.Button1.clicked.connect(self.on_click)
        
        self.ButtonDot.setText(_translate("MainWindow", "."))
        self.ButtonDot.clicked.connect(self.on_click)
        
        self.ButtonJia.setText(_translate("MainWindow", "+"))
        self.ButtonJia.clicked.connect(self.on_click)
        
        self.Button6.setText(_translate("MainWindow", "6"))
        self.Button6.clicked.connect(self.on_click)
        
        self.ButtonDel.setText(_translate("MainWindow", "Del"))
        
        self.Button5.setText(_translate("MainWindow", "5"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">0</span></p></body></html>"))

    
    def on_click(self):
        source = self.sender()
        #全部清零      
        if source.text() == 'CE':
            self.display.setText('0')
            
  
        #退格键功能
        elif source.text() == 'Del':
            if self.resultflag != 1:
                if len(self.display.text()) <=1:
                    newtext = '0'
                else:
                    newtext = self.display.text()[0:(len(self.display.text())-1)]
                self.display.setText(newtext)
                
        #计算输入的算术表达式并将结果显示
        elif source.text() == '=':
            if self.resultflag != 1:
                try:
                    disstr = self.display.text()[:]
                #考虑表达式不完整的情况处理；
                    if disstr[len(disstr)-1:] in '×÷':
                        calstr = disstr +'1'
                        #尾部为运算符+-或小数点则补0
                    elif disstr[len(disstr)-1:] in '+-.':
                        calstr = disstr + '0'
                    else:
                        calstr = disstr[:]
                    result = str(eval(calstr))
                    
                #考虑除0异常处理
                except(ZeroDivisionError,Exception) as errinfo:
                    result = 'Error:' + str(errinfo)
                    self.errflag = 1
                self.display.setText(result)
                self.resultflag = 1
            #输入数字或小数点，将算术表达式输入同步显示出来
            else:
                self.numhandle()
        
    def numhandle(self):
        rawstr = self.display.text()[:]
        strlen = len(rawstr)
        lastchar = rawstr[strlen-1 : ]
        inchar = self.sender().text()[:]
        newstr = ''
            
            #前面输入尚未计算结果
        if self.resultflag != 1:
                #当前最后一个字符为运算符
            if lasterchar in '+-×÷':
                if inchar in '0123456789':
                    newstr = rawstr + inchar
                        
                elif inchar in '+-×÷':
                    newstr = rawstr[:]
                #输入小数点，小数点前面补0再加点
                else:
                    newstr = rawstr + '0' + inchar
                        
                #当前最后一个字符为小数点
            elif lastchar == '.':
                #输入为0-9直接追加
                if inchar in '0123456789':
                    newstr = rawstr + inchar
                #输入为小数点直接忽略
                elif inchar == '.':
                    newstr = rawstr[:]
                else:
                    newstr = rawstr + '0' + inchar
                
            #当前最后一个字符为0-9
            else:
                numreg1 = re.compile(r'[+-×÷]{0，1}[0-9]+\.[0-9]*[0-9]%')
                srchrslt1 = numreg1.search(rawstr)
                 #当前最后一个数字前面已经有小数点
                if srchrslt1 != None: 
                    #输入为小数点 -> 忽略输入
                    if inchar == '.':
                        newstr = rawstr[:]
                    #输入为0-9或运算符 -> 直接追加
                    else:
                        newstr = rawstr + inchar
                
                #当前最后一个数字前面没有小数点
                else:
                    numreg2 = re.compile(r'[+\-*/]0$')
                    srchrslt2 = numreg2.search(rawstr)
                    #当前最后一个字符为0且作为最近运算符后的第一个数字
                #当前最后一个字符为0且作为最近运算符后的第一个数字
                    if srchrslt2 !=  None:
                    #输入为小数点或运算符直接添加
                        if inchar == '.' or inchar in '+-×÷':
                            newstr = rawstr + inchar
                    #输入为0-9
                        else:
                            newstr = rawstr[:]
                    #当前字符串即是'0'
                    elif rawstr == '0':
                        #输入为0-9 -> 用输入取代原字符'0'
                        if inchar in '0123456789':
                            newstr = inchar[:]
                        #输入为小数点或运算符 -> 直接追加
                        else:
                            newstr = rawstr + inchar
                    #其他情况均可直接追加
                    else:
                        newstr = rawstr + inchar
 
 
            #前面输入已经计算出结果
        else:
            #考虑计算有无异常
            if self.errflag == 0:
                #输入为运算符 -> 直接追加
                if inchar in '+-*/':
                    newstr = rawstr + inchar
                    #输入小数点 -> 以小数点前补0刷新显示
                elif inchar == '.':
                    newstr = '0' + inchar
                        #输入0-9 -> 以输入刷新显示
                else:
                    newstr = inchar[:]
            else:
                #输入为运算符 -> 忽略输入并擦除err信息
                if inchar in '+-*/':
                    newstr = '0'
                #输入小数点 -> 以小数点前补0刷新显示
                elif inchar == '.':
                    newstr = '0' + inchar
                #输入0-9 -> 以输入刷新显示
                else:
                    newstr = inchar[:]
                self.errflag = 0
                
            self.resultflag = 0
 
        self.display.setText(newstr)
 
if __name__ == '__main__':
    app =QtGui.QApplication(sys.argv)
    ex = Ui_MainWindow()
    sys.exit(app.exec_())
                
                
                    
                    
                        
                
            
                
            
            