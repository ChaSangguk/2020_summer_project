import datetime
import pickle
Time=[]   #입력받은 시간
Name = [] #입력받은 이름
Importance=[]#중요도 체크박스로 입력받을 예정


#PutTime=input("날짜를 입력하세요 : 연 월 일 순으로 입력하세요 : ")
#PutTime=PutTime.split( )#입력 받은 날짜를 띄어쓰기로 분리함.
#PutTime=list(map(int,PutTime))#문자열을 정수 형으로 변환
#PutTime.extend(PutTime_)
PutYear=int(input())
PutMonth=int(input())
PutDay=int(input())
PutHour=int(input())
PutMinute=int(input())

PutName=input()#이름 입력

PutImportance=input()


def time_(Year,Month,Day,Hour=0,Minute=0) :#시간을 입력 받고 한번에 통째로 시간으로 입력가능하게 만듦,시와 분은 빈공간으로 둘 시에 0으로 자동초기화
    return Time.append(datetime.datetime(Year,Month,Day,Hour,Minute))#Time 리스트에 입력받은 시간을 저장
def Name_(name) :
    return Name.append(PutName)
def Importance_(Importance) :
    return Importance.append(PutImportance)




try:
    with open("time.pickle","rb") as TimeData:#저장된 데이터 열기
        Time=pickle.load(TimeData)#불러오기
except :
    pass
time_(PutYear,PutMonth,PutDay,PutHour,PutMinute)
with open("time.pickle","wb") as TimeData:
    pickle.dump(Time,TimeData)#입력받은 시간값을 외부 파일에 저장




try :
    with open("Name.pickle","rb") as NameData:#저장된 데이터 열기
        Name=pickle.load(NameData)#불러오기
except:
    pass

Name_(PutName)

with open("Name.pickle","wb") as NameData:
    pickle.dump(Name,NameData)#입력받은 이름값을 NameData.pickle 파일에 저장




try:
    with open("importance.pickle","rb") as ImportanceData:#저장된 데이터 열기
        Importance=pickle.load(ImportanceData)#불러오기
except:
    pass
Importance_(PutImportance)
with open("importance.pickle","wb") as ImportanceData:
    pickle.dump(Importance,ImportanceData)#입력받은 시간값을 외부 파일에 저장


