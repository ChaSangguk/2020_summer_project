import tkinter
from tkinter import ttk
import FuncAdd as F
F.LoadBG()
F.LoadFG()
F.LoadTime1()
F.LIC()
F.LoadUC()

window3=tkinter.Tk()#설정부분


window3.title("설정")
window3.resizable(False,False)#크기 조정 불가능
window3['bg']=F.bg


bglabel=ttk.Label(window3,text='배경색 :')
bglabel.configure(background=F.bg,foreground=F.fg)
bglabel.grid(column=0,row=0)
bgEntry=ttk.Entry(window3)
bgEntry.insert(0,F.bg)
bgEntry.grid(column=1,row=0,columnspan=4)

fgLabel=ttk.Label(window3,text='글자색 :')
fgLabel.configure(background=F.bg,foreground=F.fg)
fgLabel.grid(column=0,row=1)
fgEntry=ttk.Entry(window3)
fgEntry.insert(0,F.fg)
fgEntry.grid(column=1,row=1,columnspan=4)

timeLabel=ttk.Label(window3,text='시간이')
timeLabel.configure(background=F.bg,foreground=F.fg)
timeLabel.grid(column=0,row=2)
timeEntry=ttk.Entry(window3,width=5)
timeEntry.insert(0,int(F.time1//3600))
timeEntry.grid(column=1,row=2)
time1Label=ttk.Label(window3,text='시간 남았을 때')
time1Label.configure(background=F.bg,foreground=F.fg)
time1Label.grid(column=2,row=2)

icLabel=ttk.Label(window3,text='중요 :')
icLabel.configure(background=F.bg,foreground=F.fg)
icLabel.grid(column=0,row=3)
icEntry=ttk.Entry(window3)
icEntry.insert(0,F.sibal)
icEntry.grid(column=1,row=3,columnspan=4)

ucLabel=ttk.Label(window3,text='중요하지 않음 :')
ucLabel.configure(background=F.bg,foreground=F.fg)
ucLabel.grid(column=0,row=4)
ucEntry=ttk.Entry(window3)
ucEntry.insert(0,F.uc)
ucEntry.grid(column=1,row=4,columnspan=4)

def Add():
    bg=str(bgEntry.get())
    fg=str(fgEntry.get())
    time=int(timeEntry.get())*3600
    ic=str(icEntry.get())
    uc=str(ucEntry.get())
    F.AddBG(bg)
    F.AddFG(fg)
    F.AddTime1(time)
    F.AIC(ic)
    F.AddUC(uc)
    window3.destroy()
AddButton=ttk.Button(window3,text="추가",width=10,command=Add)
AddButton.grid(column=0,row=5,columnspan=2)
CloseBtn=ttk.Button(window3,text="취소",width=10,command=window3.destroy)
CloseBtn.grid(column=3,row=5,columnspan=2)
window3.mainloop()#설정부분 끝