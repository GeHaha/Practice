# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 09:15:31 2018

@author: Gehaha

写一个运算类的接口类，所有运算继承它，
写一个输入的接口类，数字输入、小数点输入都继承

"""
import tkinter
import math
 
class Calculater:
    def __init__(self):
        #初始化主界面
        self.root = tkinter.Tk()
        self.root.title("mini计算器")
        self.root['bg'] = '#cadddb'
        self.root.minsize(270,300)
        self.root.resizable(False,False) #可调整大小
        
        #设置显示区域的值
        #self.value1() = tkinter.StringVar()
       # self.value1.set('0')
        
        #设置显示区域2的值
        #self.value2() = tkinter.StringVar()
        #self.value1.set('0')
        
        
        #定义一个变量是否按下运算符
        self.ispresign = False
        
        #定义一个变量，存储输入的数字
        self.numlist = []
        
        #定义一个记录是否按下等于号的变量
        self.isequalsign = 0
        
        #定义一个变量是否按下特殊符号的变量
        self.specilasign = 0
        
        #调用界面布局的
        self.show()
        self.root.mainloop()
    
    
    #界面布局
    def show(self):
        #数字按钮
        button0  = tkinter.Button(text = '0',command = lambda:self.pressnum('0'))
        button0.place(x=10,y=250,width = 95,height = 40)
        
        button1 = tkinter.Button(text = '1',command = lambda:self.pressnum('1'))
        button1.place(x= 10,y = 205,width = 45,height = 40)
        
        button2 = tkinter.Button(text='2', command=lambda: self.pressnum('2'))
        button2.place(x=60, y=205, width=45, height=40)

        button3 = tkinter.Button(text='3', command=lambda: self.pressnum('3'))
        button3.place(x=110, y=205, width=45, height=40)

        button4 = tkinter.Button(text='4', command=lambda: self.pressnum('4'))
        button4.place(x=10, y=160, width=45, height=40)

        button5 = tkinter.Button(text='5', command=lambda: self.pressnum('5'))
        button5.place(x=60, y=160, width=45, height=40)

        button6 = tkinter.Button(text='6', command=lambda: self.pressnum('6'))
        button6.place(x=110, y=160, width=45, height=40)

        button7 = tkinter.Button(text='7', command=lambda: self.pressnum('7'))
        button7.place(x=10, y=115, width=45, height=40)

        button8 = tkinter.Button(text='8', command=lambda: self.pressnum('8'))
        button8.place(x=60, y=115, width=45, height=40)

        button9 = tkinter.Button(text='9', command=lambda: self.pressnum('9'))
        button9.place(x=110, y=115, width=45, height=40)
        
        #点按钮
        buttondian = tkinter.Button(text='.', command=lambda: self.pressnum('.'))
        buttondian.place(x=110, y=250, width=45, height=40)

        #运算符号按钮
        buttonjia = tkinter.Button(text='+', command=lambda: self.presign('+'))
        buttonjia.place(x=160, y=250, width=45, height=40)

        buttonjian = tkinter.Button(text='-', command=lambda: self.presign('-'))
        buttonjian.place(x=160, y=205, width=45, height=40)

        buttoncheng = tkinter.Button(text='X', command=lambda: self.presign('*'))
        buttoncheng.place(x=160, y=160, width=45, height=40)

        buttonchu = tkinter.Button(text='÷', command=lambda: self.presign('/'))
        buttonchu.place(x=160, y=115, width=45, height=40)
         
        #特殊符号
        buttondel = tkinter.Button(text='←', command=lambda: self.special('←'))
        buttondel.place(x=210, y=160, width=45, height=40)

        buttonclear = tkinter.Button(text='CE', command=lambda: self.special('CE'))
        buttonclear.place(x=210, y=115, width=45, height=40)

        buttonden = tkinter.Button(text='=', command=lambda: self.presseq('='))
        buttonden.place(x=210, y=205, width=45, height=85)
        
        #显示区
       # show1= tkinter.Label(textvariable=self.value1, anchor='se', bg='white', font=('宋体', 15),bd='10')
       # show1.place(width=245, height=110)
        #show2 = tkinter.Label(textvariable=self.value2, anchor='se', bg='white', font=('宋体', 15),bd='10')
        #show2.place(y=20, width=245, height=40)
        
        

   
#定义一个输入接口类，所有的数字和字符都由此接口继承        
class Calculater_operation:
    def pressnum(self,num):
        #获得面板上的数字
        oldnum = self.value1.get()
        #判断面板上的是否为指定的数据
        if oldnum == '除数不能为0':
            return
        else:
            #判断按下点的（.）点是否在已有的数据中
            if num == '.' and num in oldnum:
                res = oldnum
            #判断按下点的时候原有数据是否为0
            elif num =='.'and old num == '0':
                res = oldnum + '.'
            #如果面板上的数字是0,则把第一个数字存储起来
            elif oldnum == '0':
                res = num
            
            #如果不是0，则和之前的数字链接起来，给变量self.value1
            else:
                res = oldnum + num
            self.value1.set(res)
            
            

#定义一个运算接口类，所有的运算都由此继承
class Character_sign:
    
     #判断是否按下了运算符号
    def presign(self):
        #判断是否按下了运算符号
        if self.ispresign == True:
            #如果按下了符号，将面板重置0
            self.value1.set('0')
            #将按下运算符号的标志重置
            self.ispresign = False
            
    
    #判断是否按下了特殊符号
    def prespecialsign(self):
        
        #判断是否按下了等于号
        if self.isequalsign == 1:    
            self.value1.set('0')
            self.isequalsign = 0
            
            
        if self.specialsign == 1:
            
            self.value1.set('0')
            self.specialsign = 0
            
        
class sign(Character_sign):
    def presign(self,sign):
        if self.ispresign == True and self.numlist !=[]:
            self.numlist[-1] = sign
        else:
            #获得面板上的数字
            oldnum = self.value1.get()
            if oldnum == '除数不能为0':
                self.value1.set('除数不能为0')
            else:
                self.numlist.append(oldnum)
                self.numlist.append(sign)
                
                
        
        
        
class specialsign(Character_sign):
    pass

ca = Calculater()
    