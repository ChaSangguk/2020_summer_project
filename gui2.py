from functools import partial
import tkinter as tk
from tkinter import ttk
import folder #폴더를 만들거나 삭제 할때 사용
import FuncAdd as FA#데이터 추가 관련 함수
import FuncPrint as FP

List=['긴급','비긴급']


window2=tk.Tk()#입력 창 부분


window2.title("일정 추가")
window2.geometry("400x80-400+30")
window2.resizable(False,False)#크기 조정 불가능
window2.configure(background='snow')


NameLabel=ttk.Label(window2, text="이름 :")
NameLabel.configure(background='snow')
NameLabel.grid(column=0,row=0)
NameEntry=ttk.Entry(window2,width=40)
NameEntry.grid(column=1,row=0,columnspan=8)

YearLabel=ttk.Label(window2, text='년 :')
YearLabel.configure(background='snow')
YearLabel.grid(column=0,row=1)
YearCombobox=ttk.Combobox(window2,width=6,state='readonly')
YearCombobox['values']=tuple(range(2020,2031))
YearCombobox.grid(column=1,row=1)
YearCombobox.current(0)


MonthLabel=ttk.Label(window2, text='월 :')
MonthLabel.configure(background='snow')
MonthLabel.grid(column=2,row=1)
MonthCombobox=ttk.Combobox(window2,width=3,state='readonly')
MonthCombobox['values']=tuple(range(1,13))
MonthCombobox.grid(column=3,row=1)
MonthCombobox.current(0)

DayLabel=ttk.Label(window2, text='일 :')
DayLabel.configure(background='snow')
DayLabel.grid(column=4,row=1)
DayCombobox=ttk.Combobox(window2,width=3,state='readonly')
DayCombobox['values']=tuple(range(1,32))
DayCombobox.grid(column=5,row=1)
DayCombobox.current(0)

HourLabel=ttk.Label(window2, text='분 :')
HourLabel.configure(background='snow')
HourLabel.grid(column=6,row=1)
HourCombobox=ttk.Combobox(window2,width=3,state='readonly')
HourCombobox['values']=tuple(range(0,24))
HourCombobox.grid(column=7,row=1)
HourCombobox.current(0)


MinuteLabel=ttk.Label(window2, text='일 :')
MinuteLabel.configure(background='snow')
MinuteLabel.grid(column=8,row=1)
MinuteCombobox=ttk.Combobox(window2,width=3,state='readonly')
MinuteCombobox['values']=tuple(range(0,60))
MinuteCombobox.grid(column=9,row=1)
MinuteCombobox.current(0)

ImportanceLabel=ttk.Label(window2, text='중요도')
ImportanceLabel.configure(background='snow')
ImportanceLabel.grid(column=0,row=2)
ImportanceCombobox_=ttk.Combobox(window2,state='readonly')
ImportanceCombobox_['values']=List
ImportanceCombobox_.grid(column=1,row=2,columnspan=4)
ImportanceCombobox_.current(0)

def Add():
    importance=str(ImportanceCombobox_.get())
    name=str(NameEntry.get())
    Year=int(YearCombobox.get())
    Month=int(MonthCombobox.get())
    Day=int(DayCombobox.get())
    Hour=int(HourCombobox.get())
    Minute=int(MinuteCombobox.get())
    folder.MakeFolder('pickle')
    FA.Importance_(importance)
    FA.Name_(name)
    FA.Time_(Year,Month,Day,Hour,Minute)
    window2.destroy()
def CloseWindow():
    window2.destroy()
AddButton=ttk.Button(window2,text="추가",width=4,command=Add)
AddButton.grid(column=5,row=2,columnspan=1)
CloseBtn=ttk.Button(window2,text="취소",width=5,command=CloseWindow)
CloseBtn.grid(column=7,row=2,columnspan=1)



# def Destroy():#창 닫는 함수
#     window2.destroy()
# def Add(Name,Importance,Year,Month,Day,Hour,Minute):
#     FuncAdd.AddData(Name,Importance,Year,Month,Day,Hour,Minute)
#     Destroy()
# closeButton=ttk.Button(window2,text="취소",command=window2.destroy(),width=7).grid(column=6,row=2,columnspan=2)
# AddButton=ttk.Button(window2,text="확인",command=Add(Name,Importance,Year,Month,Day,Hour,Minute),width=7).grid(column=8,row=2,columnspan=2)



window2.mainloop()#입력창 부분 끝