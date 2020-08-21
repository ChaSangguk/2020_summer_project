import tkinter  #gui 구현위해서
from tkinter import ttk
from tkinter import Menu
import FuncPrint as FP
import FuncAdd
import os
FuncAdd.LoadName()
def OpenWindow(i):
    pass

window1=tkinter.Tk()#메인부분



window1.title("일정관리 프로그램(가칭)")
window1.geometry("200x800-0+0")
window1.resizable(False,False)#크기 조정 불가능


menu = Menu(window1)
menu.add_cascade(label="추가",command=OpenWindow("gui2"))
menu.add_cascade(label="설정",command=OpenWindow("gui3"))
window1.config(menu=menu)


PrintDate = FP.Print()
for i in range(len(FuncAdd.Name)):
    PrintDate.Print(i,window1,0,0,3,0,1,2,5,0)


window1.mainloop()#메인부분 끝
