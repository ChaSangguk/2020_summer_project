import tkinter as tk
from tkinter import ttk
import folder #폴더를 만들거나 삭제 할때 사용
import FuncAdd #데이터 추가 관련 함수
from FuncPrint import PrintAdd

List=['긴급','비긴급']

window2=tk.Tk()#입력 창 부분


window2.title("일정 추가")
window2.geometry("375x75-400+30")
window2.resizable(False,False)#크기 조정 불가능
window2.configure(background='snow')


Name=PrintAdd()
Name.String('이름 :',window2,40,0,0,1,0,8)
Year=PrintAdd()
Year.Int(tuple(range(2020,2040)),'년 :',window2,6,0,1,1,1)
Month=PrintAdd()
Month.Int(tuple(range(1,13)),'월 :',window2,3,2,1,3,1)
Day=PrintAdd()
Day.Int(tuple(range(1,32)),'일 :',window2,3,4,1,5,1)
Importance=PrintAdd()
Importance.StringList(List,'중요도 :',window2,20,0,2,1,2,4)
CloseBtn=PrintAdd()

# def Destroy():#창 닫는 함수
#     window2.destroy()
# def Add(Name,Importance,Year,Month,Day,Hour,Minute):
#     FuncAdd.AddData(Name,Importance,Year,Month,Day,Hour,Minute)
#     Destroy()
# closeButton=ttk.Button(window2,text="취소",command=window2.destroy(),width=7).grid(column=6,row=2,columnspan=2)
# AddButton=ttk.Button(window2,text="확인",command=Add(Name,Importance,Year,Month,Day,Hour,Minute),width=7).grid(column=8,row=2,columnspan=2)



window2.mainloop()#입력창 부분 끝