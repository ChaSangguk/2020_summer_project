#메인 GUI의 일정부분을 표사하게 하는 함수
import tkinter as tk
from tkinter import ttk
import FuncAdd#Time변수와 Name변수 변수
import datetime as D
# import time as T
 

class Print:
    def convert(self,seconds): 
        self.day=seconds//86400
        self.day=int(self.day)
        seconds%=86400
        self.hour = int(seconds // 3600)
        seconds %= 3600
        self.minutes =int(seconds // 60)
    def DeliteBtn(self,i):
        try:
            FuncAdd.LoadTime()
            FuncAdd.LoadName()
            FuncAdd.LoadImportance()
            FuncAdd.Time.pop(i)
            FuncAdd.Name.pop(i)
            FuncAdd.Importance.pop(i)
            FuncAdd.SaveImportance()
            FuncAdd.SaveName()
            FuncAdd.SaveTime()
        except:
            pass
        
    def Print(self,i,Classname,nColumn,nRow,nColumnspan,iColumn,iRow,iColumnspan,tColumn,tRow,tColumnspan,BColumn,BRow) :
        FuncAdd.LoadTime()
        FuncAdd.LoadName()
        FuncAdd.LoadImportance()
        FuncAdd.LoadBG()
        FuncAdd.LoadFG()
        FuncAdd.LoadTime1()
        FuncAdd.LIC()
        FuncAdd.LoadUC()
        style=ttk.Style()
        style.configure('jotgatda.TLabel',foreground=FuncAdd.fg,background=FuncAdd.bg)
        style.configure('ssival.TLabel',foreground=FuncAdd.sibal,background=FuncAdd.bg)
        style.configure('schubal.TLabel',foreground=FuncAdd.uc,background=FuncAdd.bg)
        self.nameLabel=ttk.Label(Classname, text=FuncAdd.Name[i],style='jotgatda.TLabel')
        self.nameLabel.grid(column=nColumn,row=nRow+2*i,columnspan=nColumnspan)

        self.importanceLabel=ttk.Label(Classname,text=FuncAdd.Importance[i],style='jotgatda.TLabel')
        self.importanceLabel.grid(column=iColumn,row=iRow+2*i,columnspan=iColumnspan)
        if (FuncAdd.Time[i]-D.datetime.today()).total_seconds()>FuncAdd.time1:
            self.timeLabel=ttk.Label(Classname,text=FuncAdd.Time[i].strftime('%Y년 %m월 %d일 %p%I시 %M분까지'),style='jotgatda.TLabel')
            self.timeLabel.grid(column=tColumn,row=tRow+2*i,columnspan=tColumnspan)#
        elif (FuncAdd.Time[i]-D.datetime.now()).total_seconds()<0:
            self.convert(abs((FuncAdd.Time[i]-D.datetime.today()).total_seconds()))
            self.timeLabel=ttk.Label(Classname,text=(self.day,'일',self.hour,'시간' ,self.minutes,'분지남'),style='ssival.TLabel')
            self.timeLabel.grid(column=tColumn,row=tRow+2*i,columnspan=tColumnspan)#
        elif FuncAdd.Importance[i]=='중요':
            self.convert((FuncAdd.Time[i]-D.datetime.today()).total_seconds())
            self.timeLabel=ttk.Label(Classname,text=( self.day,'일',self.hour,'시간' ,self.minutes,'분남음'),style='ssival.TLabel')
            self.timeLabel.grid(column=tColumn,row=tRow+2*i,columnspan=tColumnspan)
        else:#importance[i]=='중요하지 않음'일때
            self.convert((FuncAdd.Time[i]-D.datetime.today()).total_seconds())
            self.timeLabel=ttk.Label(Classname,text=( self.day,'일',self.hour,'시간' ,self.minutes,'분남음'),style='schubal.TLabel')
            self.timeLabel.grid(column=tColumn,row=tRow+2*i,columnspan=tColumnspan)
        self.deleteButton=tk.Button(Classname,text="×",command=lambda : self.DeliteBtn(i))
        self.deleteButton.grid(column=BColumn,row=BRow+2*i)
