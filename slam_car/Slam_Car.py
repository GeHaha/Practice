# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Car.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import sys
import serial
import threading
import binascii 
from PyQt5 import QtCore, QtGui, QtWidgets
import serial.tools.list_ports
from PyQt5.QtWidgets import QFileDialog ,QDialog,QWidget
 

import numpy as np 
from matplotlib import pyplot as plt
from matplotlib import animation
from matplotlib.patches import Circle
from time import ctime

import math

import socket
import sys


from time import sleep
import multiprocessing


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1008, 732)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Recive_groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.Recive_groupBox.setGeometry(QtCore.QRect(10, 200, 191, 91))
        self.Recive_groupBox.setObjectName("Recive_groupBox")
        self.TCPgroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.TCPgroupBox.setGeometry(QtCore.QRect(10, 400, 191, 131))
        self.TCPgroupBox.setObjectName("TCPgroupBox")
        self.OpenPort = QtWidgets.QPushButton(self.centralwidget)
        self.OpenPort.setGeometry(QtCore.QRect(20, 540, 75, 23))
        self.OpenPort.setObjectName("OpenPort")
        self.ClosePort = QtWidgets.QPushButton(self.centralwidget)
        self.ClosePort.setGeometry(QtCore.QRect(110, 540, 75, 23))
        self.ClosePort.setObjectName("ClosePort")
        self.OpenFile = QtWidgets.QPushButton(self.centralwidget)
        self.OpenFile.setGeometry(QtCore.QRect(20, 570, 75, 23))
        self.OpenFile.setObjectName("OpenFile")
        self.SendFile = QtWidgets.QPushButton(self.centralwidget)
        self.SendFile.setGeometry(QtCore.QRect(110, 570, 75, 23))
        self.SendFile.setObjectName("SendFile")
        self.OpenServer = QtWidgets.QPushButton(self.centralwidget)
        self.OpenServer.setGeometry(QtCore.QRect(20, 600, 75, 23))
        self.OpenServer.setObjectName("OpenServer")
        self.ConnectServer = QtWidgets.QPushButton(self.centralwidget)
        self.ConnectServer.setGeometry(QtCore.QRect(110, 600, 75, 23))
        self.ConnectServer.setObjectName("ConnectServer")
        self.ClearRecieve = QtWidgets.QPushButton(self.centralwidget)
        self.ClearRecieve.setGeometry(QtCore.QRect(20, 630, 75, 23))
        self.ClearRecieve.setObjectName("ClearRecieve")
        self.ClearSend = QtWidgets.QPushButton(self.centralwidget)
        self.ClearSend.setGeometry(QtCore.QRect(110, 630, 75, 23))
        self.ClearSend.setObjectName("ClearSend")
        self.Send = QtWidgets.QPushButton(self.centralwidget)
        self.Send.setGeometry(QtCore.QRect(20, 660, 75, 23))
        self.Send.setObjectName("Send")
        self.AngleButton = QtWidgets.QPushButton(self.centralwidget)
        self.AngleButton.setGeometry(QtCore.QRect(800, 30, 75, 23))
        self.AngleButton.setObjectName("AngleButton")
        self.velocityButton = QtWidgets.QPushButton(self.centralwidget)
        self.velocityButton.setGeometry(QtCore.QRect(890, 30, 75, 23))
        self.velocityButton.setObjectName("velocityButton")
        self.GetLocaButton = QtWidgets.QPushButton(self.centralwidget)
        self.GetLocaButton.setGeometry(QtCore.QRect(800, 60, 75, 23))
        self.GetLocaButton.setObjectName("GetLocaButton")
        self.RightButton = QtWidgets.QPushButton(self.centralwidget)
        self.RightButton.setGeometry(QtCore.QRect(890, 60, 75, 23))
        self.RightButton.setText("")
        self.RightButton.setObjectName("RightButton")
        self.PortgroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.PortgroupBox.setGeometry(QtCore.QRect(10, 10, 191, 181))
        self.PortgroupBox.setObjectName("PortgroupBox")
        self.StopButton = QtWidgets.QPushButton(self.centralwidget)
        self.StopButton.setGeometry(QtCore.QRect(800, 90, 75, 23))
        self.StopButton.setObjectName("StopButton")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 420, 161, 100))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout_4 = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout_4.setContentsMargins(0, 0, 0, 0)
        self.formLayout_4.setObjectName("formLayout_4")
        self.TCPLab = QtWidgets.QLabel(self.layoutWidget)
        self.TCPLab.setObjectName("TCPLab")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.TCPLab)
        self.TCP_comboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.TCP_comboBox.setObjectName("TCP_comboBox")
        self.TCP_comboBox.addItem("")
        self.TCP_comboBox.addItem("")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.TCP_comboBox)
        self.ModelLab = QtWidgets.QLabel(self.layoutWidget)
        self.ModelLab.setObjectName("ModelLab")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.ModelLab)
        self.Model_comboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.Model_comboBox.setObjectName("Model_comboBox")
        self.Model_comboBox.addItem("")
        self.Model_comboBox.addItem("")
        self.Model_comboBox.addItem("")
        self.Model_comboBox.addItem("")
        self.Model_comboBox.addItem("")
        self.Model_comboBox.setItemText(4, "")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.Model_comboBox)
        self.IPLab_2 = QtWidgets.QLabel(self.layoutWidget)
        self.IPLab_2.setObjectName("IPLab_2")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.IPLab_2)
        self.IP_comboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.IP_comboBox.setObjectName("IP_comboBox")
        self.IP_comboBox.addItem("")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.IP_comboBox)
        self.IPLab = QtWidgets.QLabel(self.layoutWidget)
        self.IPLab.setObjectName("IPLab")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.IPLab)
        self.Port_comboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.Port_comboBox.setObjectName("Port_comboBox")
        self.Port_comboBox.addItem("")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.Port_comboBox)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(30, 220, 151, 62))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.formLayout_2 = QtWidgets.QFormLayout(self.layoutWidget1)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.ASCII1_radioButton = QtWidgets.QRadioButton(self.layoutWidget1)
        self.ASCII1_radioButton.setObjectName("ASCII1_radioButton")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.ASCII1_radioButton)
        self.Hex_radioButton = QtWidgets.QRadioButton(self.layoutWidget1)
        self.Hex_radioButton.setObjectName("Hex_radioButton")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.Hex_radioButton)
        self.send_checkBox = QtWidgets.QCheckBox(self.layoutWidget1)
        self.send_checkBox.setObjectName("send_checkBox")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.send_checkBox)
        self.time_checkBox = QtWidgets.QCheckBox(self.layoutWidget1)
        self.time_checkBox.setObjectName("time_checkBox")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.time_checkBox)
        self.layoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(20, 30, 171, 151))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget2)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.PorLab = QtWidgets.QLabel(self.layoutWidget2)
        self.PorLab.setObjectName("PorLab")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.PorLab)
        self.port_comboBox = QtWidgets.QComboBox(self.layoutWidget2)
        self.port_comboBox.setObjectName("port_comboBox")
        self.port_comboBox.addItem("")
        self.port_comboBox.addItem("")
        self.port_comboBox.addItem("")
        self.port_comboBox.addItem("")
        self.port_comboBox.addItem("")
        self.port_comboBox.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.port_comboBox)
        self.BaudLab = QtWidgets.QLabel(self.layoutWidget2)
        self.BaudLab.setObjectName("BaudLab")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.BaudLab)
        self.Baud_comboBox = QtWidgets.QComboBox(self.layoutWidget2)
        self.Baud_comboBox.setObjectName("Baud_comboBox")
        self.Baud_comboBox.addItem("")
        self.Baud_comboBox.addItem("")
        self.Baud_comboBox.addItem("")
        self.Baud_comboBox.addItem("")
        self.Baud_comboBox.addItem("")
        self.Baud_comboBox.addItem("")
        self.Baud_comboBox.addItem("")
        self.Baud_comboBox.addItem("")
        self.Baud_comboBox.addItem("")
        self.Baud_comboBox.addItem("")
        self.Baud_comboBox.addItem("")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.Baud_comboBox)
        self.DataLab = QtWidgets.QLabel(self.layoutWidget2)
        self.DataLab.setObjectName("DataLab")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.DataLab)
        self.Data_comboBox = QtWidgets.QComboBox(self.layoutWidget2)
        self.Data_comboBox.setObjectName("Data_comboBox")
        self.Data_comboBox.addItem("")
        self.Data_comboBox.addItem("")
        self.Data_comboBox.addItem("")
        self.Data_comboBox.addItem("")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.Data_comboBox)
        self.CheckLab = QtWidgets.QLabel(self.layoutWidget2)
        self.CheckLab.setObjectName("CheckLab")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.CheckLab)
        self.Check_comboBox = QtWidgets.QComboBox(self.layoutWidget2)
        self.Check_comboBox.setObjectName("Check_comboBox")
        self.Check_comboBox.addItem("")
        self.Check_comboBox.addItem("")
        self.Check_comboBox.addItem("")
        self.Check_comboBox.addItem("")
        self.Check_comboBox.addItem("")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.Check_comboBox)
        self.StopLab = QtWidgets.QLabel(self.layoutWidget2)
        self.StopLab.setObjectName("StopLab")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.StopLab)
        self.Stop_comboBox = QtWidgets.QComboBox(self.layoutWidget2)
        self.Stop_comboBox.setObjectName("Stop_comboBox")
        self.Stop_comboBox.addItem("")
        self.Stop_comboBox.addItem("")
        self.Stop_comboBox.addItem("")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.Stop_comboBox)
        self.StatuLab = QtWidgets.QLabel(self.layoutWidget2)
        self.StatuLab.setObjectName("StatuLab")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.StatuLab)
        self.CheckStaLab = QtWidgets.QLabel(self.layoutWidget2)
        self.CheckStaLab.setObjectName("CheckStaLab")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.CheckStaLab)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(110, 660, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(9, 301, 191, 91))
        self.groupBox.setObjectName("groupBox")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(210, 10, 571, 411))
        self.groupBox_2.setObjectName("groupBox_2")
        self.RectextEdit = QtWidgets.QTextEdit(self.groupBox_2)
        self.RectextEdit.setGeometry(QtCore.QRect(10, 20, 551, 381))
        self.RectextEdit.setStyleSheet("")
        self.RectextEdit.setObjectName("RectextEdit")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(210, 430, 571, 251))
        self.groupBox_3.setObjectName("groupBox_3")
        self.SendtextEdit = QtWidgets.QTextEdit(self.groupBox_3)
        self.SendtextEdit.setGeometry(QtCore.QRect(10, 20, 551, 221))
        self.SendtextEdit.setObjectName("SendtextEdit")
        self.ASCII2_radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.ASCII2_radioButton.setGeometry(QtCore.QRect(30, 322, 53, 16))
        self.ASCII2_radioButton.setObjectName("ASCII2_radioButton")
        self.Hex2_radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.Hex2_radioButton.setGeometry(QtCore.QRect(107, 322, 41, 16))
        self.Hex2_radioButton.setObjectName("Hex2_radioButton")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(107, 350, 64, 20))
        self.spinBox.setMaximum(100000)
        self.spinBox.setProperty("value", 1200)
        self.spinBox.setObjectName("spinBox")
        self.send_checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.send_checkBox_2.setGeometry(QtCore.QRect(30, 350, 71, 16))
        self.send_checkBox_2.setObjectName("send_checkBox_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1008, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.ClearRecieve.clicked.connect(self.RectextEdit.clear)
        self.ClearSend.clicked.connect(self.SendtextEdit.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Recive_groupBox.setTitle(_translate("MainWindow", "接收设置"))
        self.TCPgroupBox.setTitle(_translate("MainWindow", "网络通讯"))
        self.OpenPort.setText(_translate("MainWindow", "打开串口"))
        self.OpenPort.clicked.connect(self.port_open)
        
        self.ClosePort.setText(_translate("MainWindow", "关闭串口"))
        self.ClosePort.clicked.connect(self.port_close)
        
        self.OpenFile.setText(_translate("MainWindow", "打开文件"))
        self.OpenFile.clicked.connect(self.open_file)
        
        self.SendFile.setText(_translate("MainWindow", "发送文件"))
        self.SendFile.clicked.connect(self.send_file)
        
        self.OpenServer.setText(_translate("MainWindow", "开启服务器"))
        self.OpenServer.clicked.connect(self.open_server)
        
        self.ConnectServer.setText(_translate("MainWindow", "连接服务器"))
        self.ConnectServer.clicked.connect(self.connect_server)
        
        self.ClearRecieve.setText(_translate("MainWindow", "清除接收"))
        self.ClearSend.setText(_translate("MainWindow", "清除发送"))
        self.Send.setText(_translate("MainWindow", "发送"))
        self.Send.clicked.connect(self.send_data)
        
        self.AngleButton.setText(_translate("MainWindow", "移动角度"))
        self.AngleButton.clicked.connect(self.angle)
        
        self.velocityButton.setText(_translate("MainWindow", "移动速度"))
        self.velocityButton.clicked.connect(self.speed)
               
        self.GetLocaButton.setText(_translate("MainWindow", "获取位置"))
        self.PortgroupBox.setTitle(_translate("MainWindow", "串口设置"))
        self.StopButton.setText(_translate("MainWindow", "暂停"))
        self.StopButton.clicked.connect(self.pause)
        
        self.TCPLab.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">通讯方式</span></p></body></html>"))
        self.TCP_comboBox.setItemText(0, _translate("MainWindow", "TCP"))
        self.TCP_comboBox.setItemText(1, _translate("MainWindow", "UDP"))
        self.ModelLab.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">模式</span></p></body></html>"))
        self.Model_comboBox.setItemText(0, _translate("MainWindow", "TCP Server"))
        self.Model_comboBox.setItemText(1, _translate("MainWindow", "TCP Client"))
        self.Model_comboBox.setItemText(2, _translate("MainWindow", "UDP Server"))
        self.Model_comboBox.setItemText(3, _translate("MainWindow", "UDP Client"))
        self.IPLab_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">IP地址</span></p></body></html>"))
        self.IP_comboBox.setItemText(0, _translate("MainWindow", "127.0.0.1"))
        self.IPLab.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">目的端口</span></p></body></html>"))
        self.Port_comboBox.setItemText(0, _translate("MainWindow", "8000"))
        self.ASCII1_radioButton.setText(_translate("MainWindow", "ASCII"))
        self.Hex_radioButton.setText(_translate("MainWindow", "Hex"))
        self.send_checkBox.setText(_translate("MainWindow", "显示发送"))
        self.time_checkBox.setText(_translate("MainWindow", "显示时间"))
        self.PorLab.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">端口</span></p></body></html>"))
        self.port_comboBox.setItemText(0, _translate("MainWindow", "COM1"))
        self.port_comboBox.setItemText(1, _translate("MainWindow", "COM2"))
        self.port_comboBox.setItemText(2, _translate("MainWindow", "COM3"))
        self.port_comboBox.setItemText(3, _translate("MainWindow", "COM4"))
        self.port_comboBox.setItemText(4, _translate("MainWindow", "COM5"))
        self.port_comboBox.setItemText(5, _translate("MainWindow", "COM6"))
        self.BaudLab.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">波特率</span></p></body></html>"))
        self.Baud_comboBox.setItemText(0, _translate("MainWindow", "1200"))
        self.Baud_comboBox.setItemText(1, _translate("MainWindow", "2400"))
        self.Baud_comboBox.setItemText(2, _translate("MainWindow", "4800"))
        self.Baud_comboBox.setItemText(3, _translate("MainWindow", "9600"))
        self.Baud_comboBox.setItemText(4, _translate("MainWindow", "14400"))
        self.Baud_comboBox.setItemText(5, _translate("MainWindow", "19200"))
        self.Baud_comboBox.setItemText(6, _translate("MainWindow", "38400"))
        self.Baud_comboBox.setItemText(7, _translate("MainWindow", "56000"))
        self.Baud_comboBox.setItemText(8, _translate("MainWindow", "57600"))
        self.Baud_comboBox.setItemText(9, _translate("MainWindow", "115200"))
        self.Baud_comboBox.setItemText(10, _translate("MainWindow", "128000"))
        self.DataLab.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">数据位</span></p></body></html>"))
        self.Data_comboBox.setItemText(0, _translate("MainWindow", "5"))
        self.Data_comboBox.setItemText(1, _translate("MainWindow", "6"))
        self.Data_comboBox.setItemText(2, _translate("MainWindow", "7"))
        self.Data_comboBox.setItemText(3, _translate("MainWindow", "8"))
        self.CheckLab.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">校验位</span></p></body></html>"))
        self.Check_comboBox.setItemText(0, _translate("MainWindow", "N"))
        self.Check_comboBox.setItemText(1, _translate("MainWindow", "E"))
        self.Check_comboBox.setItemText(2, _translate("MainWindow", "O"))
        self.Check_comboBox.setItemText(3, _translate("MainWindow", "M"))
        self.Check_comboBox.setItemText(4, _translate("MainWindow", "S"))
        self.StopLab.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">停止位</span></p></body></html>"))
        self.Stop_comboBox.setItemText(0, _translate("MainWindow", "1"))
        self.Stop_comboBox.setItemText(1, _translate("MainWindow", "1.5"))
        self.Stop_comboBox.setItemText(2, _translate("MainWindow", "2"))
        self.StatuLab.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">状态</span></p></body></html>"))
        self.CheckStaLab.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">串口状态</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "检测串口"))
        self.pushButton.clicked.connect(self.port_check)
        
        self.groupBox.setTitle(_translate("MainWindow", "发送设置"))
        self.groupBox_2.setTitle(_translate("MainWindow", "接收区"))
        self.groupBox_3.setTitle(_translate("MainWindow", "发送区"))
        self.ASCII2_radioButton.setText(_translate("MainWindow", "ASCII"))
        self.Hex2_radioButton.setText(_translate("MainWindow", "Hex"))
        self.send_checkBox_2.setText(_translate("MainWindow", "自动发送"))
    
    def port_check(self):
        Com_List = []
        port_list = list(serial.tools.list_ports.comports())
        self.Port_comboBox.clear()
        for port in port_list:
            Com_List.append(port[0])
            self.Port_comboBox.addItem(port[0])
        if (len(Com_List) == 0):
            self.CheckStaLab.setText("没串口")
        
    def port_open(self):
        pass
    def port_close(self):
        pass
    def open_file(self):
        pass
    def send_file(self):
        pass
    def open_server(self):
        pass
    def connect_server(self):
        pass
    def send_data(self):
        pass
    def speed(self):
        pass
    def pause(self):
        pass
    def angle(self):
        pass
        
                                
#调用程序    
if __name__ == '__main__':
    
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)     
    MainWindow.show() 
    sys.exit(app.exec_()) 

