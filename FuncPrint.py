#메인 GUI의 일정부분을 표사하게 하는 함수
import tkinter as tk
from tkinter import ttk
import FuncAdd#Time변수와 Name변수 변수
import datetime as D


class Print:#클래스 이름은 창의 이름으로 해야함
    def Print(self,i) :
        nameLabel=tk.Label(self, text=FuncAdd.Name[i])
        nameLabel.pack()
        timeLabel=tk.Label(self,text=FuncAdd.Time[i].strftime('%Y년 %m월 %d일 %p%I시 %M분'))
        timeLabel.pack()
        deleteButton=tk.Button(self,text="×")
        deleteButton.pack()
class PrintAdd:
    def String(self,text,className,Width,LColumn,LRow,EColumn,ERow,Columnspan=1):
        self.Var=tk.StringVar()
        self.Label=ttk.Label(className, text=text)
        self.Label.configure(background='snow')
        self.Label.grid(column=LColumn,row=LRow)
        self.Entry=ttk.Entry(className,width=Width,textvariable=self.Var)
        
        self.Entry.grid(column=EColumn,row=ERow,columnspan=Columnspan)
        self.Var=self.Var.get()
    def Int(self,List,Text,ClassName,Width,LColumn,LRow,EColumn,ERow,Columnspan=1):
        self.var=tk.IntVar()
        self.Label=ttk.Label(ClassName, text=Text)
        self.Label.configure(background='snow')
        self.Label.grid(column=LColumn,row=LRow)
        self.Combobox=ttk.Combobox(ClassName,width=Width,state='readonly',textvariable=self.var)
        self.Combobox['values']=List
        self.Combobox.grid(column=EColumn,row=ERow)
        
        self.var=self.var.get()
        self.Combobox.current(0)
    def StringList(self,List,Text,ClassName,Width,LColumn,LRow,EColumn,ERow,Columnspan=1):
        self.var=tk.StringVar()
        self.Label=ttk.Label(ClassName, text=Text)
        self.Label.configure(background='snow')
        self.Label.grid(column=LColumn,row=LRow)
        self.Combobox=ttk.Combobox(ClassName,state='readonly',textvariable=self.var)
        self.Combobox['values']=List
        self.Combobox.grid(column=EColumn,row=ERow,columnspan=Columnspan)
        
        self.var=self.var.get()
        self.Combobox.current(0)
    def Button(self):
        pass


#이 클래스를 사용할 파일 목록


window1=Print()