import tkinter
import FuncAdd as F#FuncAdd 모듈을 F로도 호출할 수 있음 예) F.Time_()
window1=tkinter.Tk()#메인부분


window1.title("일정관리 프로그램(가칭)")
window1.geometry("400x800-0+0")
window1.resizable(False,False)




window1.mainloop()

window2=tkinter.Tk()#입력 창 부분

window2.title("설정")



nameLabel=tkinter.Label(window2, text="이름")
nameLabel.pack()



window2.mainloop()


window3=tkinter.Tk()#설정부분
window3.mainloop()