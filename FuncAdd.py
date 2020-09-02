import datetime 
import pickle   
Time=[]
Name=[]
Importance = []  
bg='#ffffff'
time1=43200
sibal='#ff0000'
uc='#0000ff'
fg='#000000'
def LoadTime() :
    global Time
    try:
        with open("./pickle/time.pickle","rb") as TimeData:
            Time=pickle.load(TimeData)#불러오기
    except :#제일 처음 실행시 time.pickle파일이 없어 에러가 생기므로 이를 우회함
        pass
def AddTime(Year,Month,Day,Hour=0,Minute=0):
    global Time
    Time.append(datetime.datetime(Year,Month,Day,Hour,Minute))#Time 리스트에 입력받은 시간을 저장
def SaveTime():
    global Time
    with open("./pickle/time.pickle","wb") as TimeData:
        pickle.dump(Time,TimeData)
def Time_(Year,Month,Day,Hour=0,Minute=0):
    LoadTime()
    AddTime(Year,Month,Day,Hour,Minute)
    SaveTime()
def LoadName() :
    global Name
    try :
        with open("./pickle/Name.pickle","rb") as NameData:
            Name=pickle.load(NameData)
    except:
        pass
def AddName(name):
    global Name
    Name.append(name)
def SaveName():
    global Name
    with open("./pickle/Name.pickle","wb") as NameData:
        pickle.dump(Name,NameData)
def Name_(name):
    LoadName()
    AddName(name)
    SaveName()
def LoadImportance() :
    global Importance
    try:
        with open("./pickle/importance.pickle","rb") as ImportanceData:
            Importance=pickle.load(ImportanceData)
    except:
        pass
def AddImportance(importance):
    global Importance
    Importance.append(importance)
def SaveImportance():
    global Importance
    with open("./pickle/importance.pickle","wb") as ImportanceData:
        pickle.dump(Importance,ImportanceData)
def Importance_(importance):
    LoadImportance()
    AddImportance(importance)
    SaveImportance()




def AddBG(BG):

    with open('./pickle/bg.pickle','wb') as bg_:
        pickle.dump(BG,bg_)
def LoadBG():
    global bg
    try:
        with open('./pickle/bg.pickle','rb')as bg_:
            bg=pickle.load(bg_)
    except:
        pass
def LoadTime1():
    global time1
    try:
        with open('./pickle/time1.pickle','rb') as t:
            time1=pickle.load(t)
    except:
        pass
def AddTime1(T):
    with open('./pickle/time1.pickle','wb') as t:
        pickle.dump(T,t)
def AIC(IC):
    with open('./pickle/IC.pickle','wb') as c:
        pickle.dump(IC,c)
def LIC():
    global sibal
    try:
        with open('./pickle/ic.pickle','rb')as ic:
            sibal=pickle.load(ic)
    except:
        pass
def AddUC(uc):
    with open('./pickle/UC.pickle','wb') as u:
        pickle.dump(uc,u)
def LoadUC():
    global uc
    try:
        with open('./pickle/UC.pickle','rb') as u:
            uc=pickle.load(u)
    except:
        pass
def AddFG(fg):
    with open('./pickle/FG.pickle','wb') as f:
        pickle.dump(fg,f)
def LoadFG():
    global fg
    try:
        with open('./pickle/FG.pickle','rb') as f:
            fg=pickle.load(f)
    except:
        pass