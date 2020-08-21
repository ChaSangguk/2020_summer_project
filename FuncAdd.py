#데이터를 추가하고 그 데이터를 저장하는 함수의 모음

import datetime #시간저장을 위해서 임포트함
import pickle   #입력 받은 데이터를 프로그램 종료 후에도 저장을 위해서 임포트
Time=[]    #입력받은 시간을 저장할 리스트
Name=[]    #입력받은 이름을 저장할 리스트
Importance = []    #중요도를 저장하는 리스트(체크박스로 입력받을 예정)
def LoadTime() :#시간을 입력받게 만듦 
    global Time
    try:
        with open("./pickle/time.pickle","rb") as TimeData:#저장된 데이터 열기
            Time=pickle.load(TimeData)#불러오기
    except :#제일 처음 실행시 time.pickle파일이 없어 에러가 생기므로 이를 우회함
        pass
def AddTime(Year,Month,Day,Hour=0,Minute=0):
    global Time
    Time.append(datetime.datetime(Year,Month,Day,Hour,Minute))#Time 리스트에 입력받은 시간을 저장
def SaveTime():
    global Time
    with open("./pickle/time.pickle","wb") as TimeData:#time.pickle이라는 파일을 바이너리 쓰기전용으로 호출함 
        pickle.dump(Time,TimeData)#입력받은 시간값을 외부 파일에 저장
def Time_(Year,Month,Day,Hour=0,Minute=0):
    LoadTime()
    AddTime(Year,Month,Day,Hour=0,Minute=0)
    SaveTime()
def LoadName() :
    global Name
    try :
        with open("./pickle/Name.pickle","rb") as NameData:#저장된 데이터 열기
            Name=pickle.load(NameData)#불러오기
    except:
        pass
def AddName(name):
    global Name
    Name.append(name)
def SaveName():
    global Name
    with open("./pickle/Name.pickle","wb") as NameData:
        pickle.dump(Name,NameData)#입력받은 이름값을 NameData.pickle 파일에 저장
def Name_(name):
    LoadName()
    AddName(name)
    SaveName()
def LoadImportance() :
    global Importance
    try:
        with open("./pickle/importance.pickle","rb") as ImportanceData:#저장된 데이터 열기
            Importance=pickle.load(ImportanceData)#불러오기
    except:
        pass
def AddImportance(importance):
    global Importance
    Importance.append(importance)
def SaveImportance():
    global Importance
    with open("./pickle/importance.pickle","wb") as ImportanceData:
        pickle.dump(Importance,ImportanceData)#입력받은 시간값을 외부 파일에 저장
def Importance_(importance):
    LoadImportance()
    AddImportance(importance)
    SaveImportance()
