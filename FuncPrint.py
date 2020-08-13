#메인 GUI의 일정부분을 표사하게 하는 함수
import tkinter
import FuncAdd
def PrintData() :
    for i in range(len(FuncAdd.Time)):   #입력 받은 일정을 모두 메인에 표시해야 하므로 입력받은 데이터의 개수만큼 반복함
        #출력부분 구현 예정