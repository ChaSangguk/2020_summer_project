import tkinter  #gui 구현위해서
from tkinter import ttk

import FuncPrint as FP
import FuncAdd

window1=tkinter.Tk()#메인부분



window1.title("일정관리 프로그램(가칭)")
window1.geometry("400x800-0+0")
window1.resizable(False,False)#크기 조정 불가능


for i in range(len(FuncAdd.Name)):
    FP.window1.Print(i)

window1.mainloop()#메인부분 끝
