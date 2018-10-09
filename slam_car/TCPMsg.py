# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 13:49:23 2018

@author: Gehaha
"""
import binascii
import threading
from SlamCar import Ui_MainWindow
import serial.tools.list_ports
from PyQt5.QtNetwork import QTcpSocket
import socket


import sys
import serial

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import QFileDialog ,QDialog,QWidget
from time import ctime

import math
import multiprocessing

#定义Tcp通讯类
class TcpMsg(QtWidgets.QMainWindow,Ui_MainWindow):
    socket = QTcpSocket() 
    def __init__(self):
        super(TcpMsg,self).__init__()
        self.setupUi(self)
        self.OpenServer.clicked.connect(self.open_server)
        self.ConnectServer.clicked.connect(self.connect_server)       
        self.Send.clicked.connect(self.send_data)
            
    #作为客户端端，连接服务器
   
    def connect_server(self):
        self.model = self.TCP_comboBox.currentText()
        self.BUFSIZE = 1024
        self.address = ('127.0.0.1')
        self.port = 8888# 服务器的端口
        self.client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)       
        #连接服务器
        self.client.connect(self.address,self.port)
        self.CheckStaLab.setText("连接成功")
        
    #要添一个发送请求的按钮
    
    def send_request(self):
        self.model = self.TCP_comboBox.currentText()
        self.BUFSIZE = 1024
        self.address = ('127.0.0.1')
        self.port = 8888# 服务器的端口
        self.client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        
        #while循环时为保证能持续进行数据传输
        while True:
            #发送数据
            self.send_data =  self.SendtextEdit.setText()
            if(self.Hex2_radioButton.isChecked()):
                self.SendtextEdit.write(binascii.a2b_hex(self.SendtextEdit.toPlainText()))
            else:
                self.SendtextEdit.write(self.SendtextEdit.toPlainText().encode('utf-8'))
            self.client.send(self.send_data.encode())
        
            recv_data = self.client.recv(self.BUFSIZE).decode('utf-8') # 接受服务器端的数据         
            if not recv_data:
                break
            else:
                self.RectextEdit.append(recv_data)
                self.RectextEdit.setText(recv_data)
        self.client.close()
                
    #作为服务器端，打开服务器
    def open_server(self):
        
        self.address = '127.0.0.1'
        self.port = 8888
        self.buffsize = 1024 #接收客户端发来的数据缓存区大小
        server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        server.bind((self.address,self.port))
        server.listen(2) #最大连接数
        
        #设置退出条件
        stop_connect = False
        while not stop_connect:
            self.RectextEdit.setText("等待连接客户端.....")
            self.clientsock,clientaddress = server.accept()
            self.RectextEdit.setText("连接客户端：",self.clientaddress)
            while True:
                try:
                    recvdata =self.clientsock.recv(self.buffsize.decode('utf-8'))
                    self.RectextEdit.setText("连接客户端：",recvdata)
                except:
                    self.RectextEdit.setText("连接客户端：无数据")
                    break
                if not recvdata:
                    break
                sendata = "服务器端发来：" + recvdata
                self.clientsock.recv(sendata.encode('utf-8'))
                self.RectextEdit.setText(sendata)
                stop_connect = '0'
                if stop_connect:
                    break
                self.clientsock.close()
                self.server.close()
                
                
if __name__ == "__main__":
    app = QtWidgets.QMainWindow()
    ui = TcpMsg()     
    ui.show() 
    sys.exit(app.exec_())          
                    
        
        
      
    
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    