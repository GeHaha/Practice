# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 11:16:50 2018

@author: Gehaha
"""
from Car import Ui_MainWindow
import binascii
import threading
import serial.tools.list_ports
import socket
from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtWidgets import QFileDialog ,QDialog,QWidget
 

class serial_data(Ui_MainWindow):
    ser = serial.Serial()
    
    #检查串口
    def port_check(self):
        Com_List = []
        port_list = list(serial.tools.list_ports.comports())
        self.Port_comboBox.clear()
        for port in port_list:
            Com_List.append(port[0])
            self.Port_comboBox.addItem(port[0])
        if (len(Com_List) == 0):
            self.CheckStaLab.setText("没串口")
            
                
    #打开串口
    def prot_open(self):
        self.ser.port = self.Port_comboBox.currentText()
        self.ser.baudrate = self.Baud_comboBox.currentText()
        self.ser.bytesize = int(self.Data_comboBox.currentText())
        self.ser.stopbits = int(self.Stop_comboBox.currentText())
        self.ser.parity = self.Check_comboBox.currentText()
        self.ser.open()
        if (self.ser.isOpen()):
            self.OpenPort.setEnabled(False) #打开不成功
            self.CheckStaLab.setText("打开成功")
            self.t1 = threading.Thread(target = self.receive_data)
            #isdaemon()判断
            self.t1.setDaemon(True)
            self.t1.start()
        else:
            self.CheckStaLab.setText("打开失败")
            
    #关闭串口
    def port_close(self):
        self.ser.close()
        if (self.ser.isOpen()):
            self.CheckStaLab.setText("关闭失败")
        else:
            self.OpenPort.setEnabled(True)
            self.CheckStaLab.setText("关闭成功")
    #发送数据
    def send_data(self):
        #串口接收数据
        if(self.ser.isOpen):          
            if(self.Hex2_radioButton.isChecked()):
                self.ser.write(binascii.a2b_hex(self.SendtextEdit.toPlainText()))
            else:
                self.ser.write(self.SendtextEdit.toPlainText().encode('utf-8'))
            self.CheckStaLab.setText("发送成功")
        else:
            self.CheckStaLab.setText("发送失败")
                  
    #接收数据
    def receive_data(self):
        print("receive data threading is start")
        res_data = ''
        #接收次数，初始为0，每接收一次增加一次
        num = 0 
        while(self.ser.isOpen()):
            size = self.ser.inWaiting()
            if size:
                res_data = self.ser.read_all()
                if(self.Hex2_radioButton.isChecked()):
                    self.RectextEdit.append(binascii.b2a_hex(res_data).decode())
                else:
                    self.RectextEdit.append(res_data.decode())
                self.RectextEdit.moveCursor(QtGui.QTextCursor.End)
                self.ser.flushInput()
                num += 1
                self.CheckStaLab.setText("接收:" + str(num))
                
    #发送文件
    def send_file(self):
        if (self.ser.isOpen()):
            if(self.Hex2_radioButton.isChecked()):
                self.ser.write(binascii.a2b_hex(self.SendtextEdit.toPlainText()))
            else:
                self.ser.write(self.SendtextEdit.toPlainText().encode('utf-8'))
            self.CheckStaLab.setText("发送成功")
        else:
            self.CheckStaLab.setText("发送失败")
            
    #打开文件
    def open_file(self):
        filename = QFileDialog.getOpenFileName(self,"打开文件","./","All Files (*);;Text Files (*.)")
        if filename[0]:
            f = open(filename[0],'r')
            with f:
                data = f.read()
                self.SendtextEdit.setText(data)
    
            
