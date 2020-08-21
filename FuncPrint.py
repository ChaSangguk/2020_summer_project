#메인 GUI의 일정부분을 표사하게 하는 함수
import tkinter as tk
from tkinter import ttk
import FuncAdd#Time변수와 Name변수 변수
import datetime as D


class Print:
    def Print(self,i,Classname,nColumn,nRow,nColumnspan,tColumn,tRow,tColumnspan,BColumn,BRow) :
        FuncAdd.LoadTime()
        FuncAdd.LoadName()
        FuncAdd.LoadImportance()
        print(FuncAdd.Time)
        print(FuncAdd.Name)
        print(FuncAdd.Importance)
        self.nameLabel=ttk.Label(Classname, text=FuncAdd.Name[i])
        self.nameLabel.grid(column=nColumn,row=nRow+2*i,columnspan=nColumnspan)#
        if 1==1:
            self.timeLabel=ttk.Label(Classname,text=FuncAdd.Time[i].strftime('%Y년 %m월 %d일 %p%I시 %M분'))
            self.timeLabel.grid(column=tColumn,row=tRow+2*i+1,columnspan=tColumnspan)#
        else:
            self.timeLabel=ttk.Label(Classname,text="")
        self.deleteButton=tk.Button(Classname,text="×",command="")
        self.deleteButton.grid(column=BColumn,row=BRow+2*i)
