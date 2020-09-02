import tkinter  #gui 구현위해서
from tkinter import ttk
from tkinter import Menu
import FuncPrint as FP
import FuncAdd
import os
FuncAdd.LoadName()
window1=tkinter.Tk()#메인부분



window1.title("일정관리 프로그램")
window1.geometry("320x800-0+0")
window1.resizable(False,False)#크기 조정 불가능
FuncAdd.LoadBG()
window1['bg']=FuncAdd.bg
def OpenWindow1():
    path=os.getcwd()+'\\add.py'
    os.system(path)

def OpenWindow2():
    path=os.getcwd()+'\\setting.py'
    os.system(path)

menu = Menu(window1)
menu.add_cascade(label="추가",command=OpenWindow1)
menu.add_cascade(label="설정",command=OpenWindow2)

window1.config(menu=menu)

a=FP.Print()
PrintDate = FP.Print()
for i in range(len(FuncAdd.Name)):
    a.Print(i,window1,0,0,3,4,0,2,0,1,2,8,0)



window1.mainloop()#메인부분 끝
