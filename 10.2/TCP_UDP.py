# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 13:49:23 2018

@author: Gehaha
"""
import binascii
import threading
from Car import Ui_MainWindow
import serial.tools.list_ports
from PyQt5.QtNetwork import QTcpSocket
import socket
from PyQt5.QtNetwork import QTcpSocket

class Tcp_UDP(Ui_MainWiondow):

    
    #作为客户端端，连接服务器
    def client(self):
        self.ser.model = self.TCP_comboBox.currentText()
        self.BUFSIZE = 1024
        self.address = ('127.0.0.1')
        self.port = 8888# 服务器的端口
        self.client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        
        #连接服务器
        self.client.connect(self.address,self.port)
        self.CheckStaLab.setText("连接成功")
    def send_request(self):
        #while循环时为保证能持续进行数据传输
        while True:            
            self.data =  self.SendtextEdit.setText()
            if(self.Hex2_radioButton.isChecked()):
                self.SendtextEdit.write(binascii.a2b_hex(self.SendtextEdit.toPlainText()))
            else:
                self.SendtextEdit.write(self.SendtextEdit.toPlainText().encode('utf-8'))
            self.CheckStaLab.setText("连接成功")
    #作为服务器端，打开服务器
    def open_server(self):
        socket = QTcpSocket()
        if not socket.setSocketDescriptor(self.socketId):
            self.
    
        
    