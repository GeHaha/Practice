# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from PyQt5 import QtCore, QtGui, QtWidgets
import serial.tools.list_ports
from PyQt5.QtWidgets import QFileDialog ,QDialog,QWidget
 

import numpy as np 
from matplotlib import pyplot as plt
from matplotlib import animation
from matplotlib.patches import Circle
from time import ctime
from Calculator import Ui_MainWindow

import math


class MyMainWindow(QMainWindow,Ui_MainWindow):
    
    def button_link(self):
        self.Button0.clicked.connect(self.button_event(0))
        self.Button1.clicked.connect(self.button_event(1))
        self.Button2.clicked.connect(self.button_event(2))
        self.Button3.clicked.connect(self.button_event(3))
        self.Button4.clicked.connect(self.button_event(4))
        self.Button5.clicked.connect(self.button_event(5))
        self.Button6.clicked.connect(self.button_event(6))
        self.Button7.clicked.connect(self.button_event(7))
        self.Button8.clicked.connect(self.button_event(8))
        self.Button9.clicked.connect(self.button_event(9))
        self.ButtonJia.clicked.connect(self.button_event('+'))
        self.ButtonJian.clicked.connect(self.button_event('-'))
        self.ButtonCheng.clicked.connect(self.button_event('×'))
        self.ButtonChu.clicked.connect(self.button_event('÷'))
        self.ButtonDeng.clicked.connect(self.button_event('='))
        self.ButtonDot.clicked.connect(self.button_event('.'))
        self.ButtonDel.clicked.connect(self.del_num)
        self.ButtonCE.clicked.connect(self.clear_num)
        
    def __init__(self,parent = None):
        super(MyMainWindow,self).__init__(parent)
        self.setupUi(self)
        self.button_link() #连接信号
        
    def button_event(self,arg):
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        