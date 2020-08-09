from tkinter import *
root = Tk()
root.title()

name_label= Label(root,text="이름")
name_=Entry(root, width=30)
name_label.pack()
name_.pack()
 
def subbmit() :
    PutName=name_.get()#이름 저장
    name_.delete(0,END)#이름 지우기


butn = Button(root,text="제출",command=subbmit)
butn.pack()
root.mainloop()