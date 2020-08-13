import tkinter
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