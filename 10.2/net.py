# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 13:49:23 2018

@author: Gehaha
"""

class Tcp_UDP(Ui_MainWiondow):
    
    #作为客户端端，连接服务器
    def connect_server(self):
        self.ser.model = self.TCP_comboBox.currentText()
        self.BUFSIZE = 1024
        self.address = ('127.0.0.1')
        self.port = 8888# 服务器的端口
        self.client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        
        #连接服务器
        self.client.connect(addresss,port)
        #while循环时为保证能持续进行数据传输
        while True:
            self.data =  self.SendtextEdit.setText(data)
            if(self.Hex2_radioButton.isChecked()):
                self.ser.write(binascii.a2b_hex(self.SendtextEdit.toPlainText()))
            else:
                self.ser.write(self.SendtextEdit.toPlainText().encode('utf-8'))
            self.CheckStaLab.setText("发送成功")
    #作为服务器端，打开服务器
    def open_server(self):
        pass
    
        
    