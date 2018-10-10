# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 11:16:50 2018

@author: Gehaha
"""
import sys
from SlamCar3 import Ui_MainWindow
import binascii
import threading
import serial
import socket
from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtWidgets import QFileDialog ,QDialog,QWidget
sys.path.append('D:\Practice\10.2')

#逻辑部分
class SignalLogic(QtWidgets.QMainWindow,Ui_MainWindow):
    ser = serial.Serial()
    def __init__(self):  #析构函数，实例化后默认加载
        super(SignalLogic,self).__init__()  #超级加载
        self.setupUi(self)
        
        self.OpenPort.clicked.connect(self.port_open)
        self.ClosePort.clicked.connect(self.port_close)
        self.pushButton.clicked.connect(self.port_check)
        self.OpenFile.clicked.connect(self.open_file)
        self.SendFile.clicked.connect(self.send_file)
        self.Send.clicked.connect(self.send_data)
        self.OpenServer.clicked.connect(self.open_server)
        self.ConnectServer.clicked.connect(self.connect_server)
        self.GetLocaButton.clicked.connect(self.get_location)
        self.sendMsgButton.clicked.connect(self.send_message)
        
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
    def port_open(self):
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
            self.ClosePort.setEnabled(True)
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
    def open_server(self,sock,addr):
        
        self.address = '127.0.0.1'
        self.port = 8888
        self.buffsize = 1024 #接收客户端发来的数据缓存区大小
        self.server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.server.bind((self.address,self.port))
        self.server.listen(2) #最大连接数
        
        #设置退出条件
        stop_connect = False
        while not stop_connect:
            self.clientsock,self.clientaddress = self.server.accept()
            self.RectextEdit.setText("等待连接客户端.....")
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
    def send_message(self):
        pass
    
#程序调用界面                
#调用程序    
if __name__ == '__main__':
    
    app = QtWidgets.QApplication(sys.argv) #外部参数列表
    MainWindow = QtWidgets.QMainWindow()  # 
    ui = SignalLogic()  
    ui.show() 
    sys.exit(app.exec_())  #退出中使用的消息循环，结束消息循环时就退出程序


