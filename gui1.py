import tkinter  #gui 구현위해서
import FuncAdd #데이터 추가 관련 함수
import folder #폴더를 만들거나 삭제 할때 사용
window1=tkinter.Tk()#메인부분



window1.title("일정관리 프로그램(가칭)")
window1.geometry("400x800-0+0")
window1.resizable(False,False)#크기 조정 불가능




window1.mainloop()#메인부분 끝

window2=tkinter.Tk()#입력 창 부분
window2.title("일정 추가")




nameLabel=tkinter.Label(window2, text="이름")
nameLabel.pack()
YearLabel=tkinter.Label(window2, text="연도")
YearLabel.pack()
MonthLabel=tkinter.Label(window2, text="월")
MonthLabel.pack()
DayLabel=tkinter.Label(window2, text="일")
DayLabel.pack()
ImportanceLabel=tkinter.Label(window2, text="중요도")
ImportanceLabel.pack()




window2.mainloop()#입력창 부분 끝


window3=tkinter.Tk()#설정부분
window3.title("설정")
window3.mainloop()#설정부분 끝