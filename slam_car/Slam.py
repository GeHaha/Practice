# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 12:22:08 2018

@author: Gehaha
"""
from SlamCar2 import Ui_MainWindow
import serial
import binascii
import serial.tools.list_ports
import socket
from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtWidgets import QFileDialog ,QDialog,QWidget
from math import radians ,copysign
import rospy


#小车调度系统
class slam_car(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(slam_car,self).__init__()
        self.setupUi(self)
        self.OpenFile.clicked.connect(self.open_file)
        self.SendFile.clicked.connect(self.send_file)
        
        self.GetLocaButton.clicked.connect(self.get_location)
        self.sendMsgButton.connect(self.send_message)
        

    #得到位置信息
    def get_location(self):
        
        #首先要检查出口是否打开
        if(self.ser.isOpen()):        
            if(self.Hex2_radioButton.isChecked()):
                self.ser.write(binascii.a2b_hex(self.SendtextEdit.toPlainText('0x10')))
            else:
                self.ser.write(self.SendtextEdit.toPlainText('0x10').encode('utf-8'))
            self.CheckStaLab.setText("开始获取位置信息")
        else:
            self.CheckStaLab.setText("位置获取失败")
      
    def recieve_location(self):
        #假如定义一个头部信息
        head_data = [0x10,0x20,0x30]     
        location_data = []
      
        self.RectextEdit.setText("接收位置信息：" + str())
        while(self.ser.isOpen()):           
            size = self.ser.inWaiting() #获取接收缓存区的字节数           
            if size:
                res_data = self.ser.read_all()
                if (self.Hex2_radioButton.isCheckd()):
                    self.RectextEdit.append(binascii.b2a_hex(res_data).decode())
                    #如果接收到的数据对的就保存，错的就放弃
                    if (res_data[:3] == head_data):
                        pass
                    else:
                        self.ser.inWaiting.clear()
                else:
                    self.RectextEdit.append(res_data.decode())
                self.RectextEdit.moveCursor(QtGui.QTextCursor.End)
                #怎么验证CRC                
                self.ser.flushInput()
   # 发送小车需要的角度、速度、坐标 
    def send_message(self):
        pass
   
     
    
    