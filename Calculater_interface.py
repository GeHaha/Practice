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
        self.value1 = tkinter.StringVar()
        self.value1.set('0')
        
        #设置显示区域2的值
        self.value2 = tkinter.StringVar()
        self.value1.set('0')
        
        
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
        show1= tkinter.Label(textvariable=self.value1, anchor='se', bg='white', font=('宋体', 15),bd='10')
        show1.place(width=245, height=110)
        show2 = tkinter.Label(textvariable=self.value2, anchor='se', bg='white', font=('宋体', 15),bd='10')
        show2.place(y=20, width=245, height=40)
                
#定义一个输入接口类，所有的数字和字符都由此接口继承        
class Calculater_operation(Calculater):
    def pressnum(self,num):
        pass


class getnum(Calculater_operation):
    
    def pressnum(self,num):
         # 判断是否按下了运算符号
        if self.ispresign == True:
            # 如果按下了符号，将面板数字重置为 0
            self.value1.set('0')
            # 将按下运算符号的标志重置
            self.ispresign = False            
        # 判断是否按下了等于号
        if self.isequalsign == 1:
            self.value1.set('0')
            self.isequalsign = 0
            
        #判断是否按下了特殊符号    
        if self.specialsign == 1:
            self.value1.set('0')
            self.specialsign = 0
            
        # 获得面板上的数字
        oldnum = self.value1.get()
        
        # 判断面板上的是否为指定的数据
        if oldnum == '除数不能为0':
            return
        else:
            # 判断按下的(.)点是否在已有数据中
            if num == '.' and num in oldnum:
                res = oldnum
                
            # 判断按下点的时候原有数据是否为0
            elif num == '.' and oldnum == '0':
                res = oldnum + '.'
                
            # 如果面板上的数字是0，则把第一个数字储存起来
            elif oldnum == '0':
                res = num
                
            # 如果不是0，则和之前的数字链接起来，给变量self.value1
            else:
                res = oldnum + num
            self.value1.set(res)
            
            
#定义一个运算接口类，所有的运算都由此继承
class Character_sign(Calculater):
    def presign(self,sign):
        pass
    def special(self,sign):
        pass
    def presseq(self,signeq):
        pass

# 按下运算符号的函数()    
class getsign(Character_sign):
    
    def presign(self,sign):      
     # 判断之前是否已经按过运算符号
        if self.ispresign == True and self.numlist != []:  # True  表示上一次按过运算符号
            self.numlist[-1] = sign  # 把第二次按的运算符号替换成上次的运算符号
        else:
            # 获得面板上的数字
            oldnum = self.value1.get()
            if oldnum == '除数不能为0':
                self.value1.set('除数不能为0')
            else:
                # 先将面板上的数字储存到列表中
                self.numlist.append(oldnum)
                # 再将按下的符号储存到列表
                self.numlist.append(sign)
        # 按下符号，会将按下符号标志的状态记录下来
        self.ispresign = True

        
#按下特殊符号的按钮 （C清空所有，CE清空当前，消除最后一位）   
class specialsign(Character_sign):
      
    #判断是否按下了特殊符号
    def special(self,sign):
        # 获得当前面板上的内容
        strs = self.value1.get()
        
        if sign == 'CE':
            # 直接清空列表
            self.numlist.clear()
            
            self.value2.set('')
            # 将面板上的置为0
            res = 0
        elif sign == '←':
            if strs != '除数不能为0':
                # 判断面板上数字是否为0
                if strs != '0':
                    # 判断面板上数字是否就一位数
                    if len(strs) != 1:
                        # 进行切片操作
                        res = strs[0:-1]
                    else:
                        # 如果就一位数字直接变为0
                        res = '0'
                    if self.isequalsign == 1:
                        res = strs
                else:
                    # 若等于0 则不进行操作
                    res = '0'
            else:
                res = strs

        # 将是否按下特殊符号的标志置为已按（用1表示）
        self.specialsign = 1
        # 将上面处理的数字放到面板中
        self.value1.set(res)
        
# 计算结果       
class getres(Character_sign):
    def presseq(self,signeq):
        # 获得面板上数字
        oldnum = self.value1.get()
        if self.isequalsign == 1:
            self.value1.set(oldnum)
            self.isequalsign = 0
            
        elif self.specialsign == 1:
            self.value1.set(oldnum)
            self.specialsign = 0
            
        elif self.numlist == []:
            self.value1.set(oldnum)
            
        else:
            if oldnum == '除数不能为0':
                self.value1.set(oldnum)
            else:
                # 判断进行除法操作的时候，除数是否为0
                if self.numlist[-1] == '/' and eval(oldnum) == 0:
                    self.value1.set('除数不能为0')
                    self.numlist.clear()
                else:
                    # 将获得的数字添加到列表中
                    self.numlist.append(oldnum)
                    # 将列表中的字符串连接成字符串
                    result = ''.join(self.numlist)
                    # 将连接的字符串进行运算
                    self.value1.set(eval(result)) 
                    #将运算过程显示到屏幕2
                    self.value2.set(result)
                    
                    # 清空列表
                    self.numlist.clear()
        # 将是否按下等号的标志设置为已按（用1表示）
        self.isequalsign = 1
        
ca = Calculater()
    