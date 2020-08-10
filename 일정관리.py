import datetime
Time=[]   #입력받은 시간
Name = [] #입력받은 이름



#PutTime=input("날짜를 입력하세요 : 연 월 일 순으로 입력하세요 : ")
#PutTime=PutTime.split( )#입력 받은 날짜를 띄어쓰기로 분리함.
#PutTime=list(map(int,PutTime))#문자열을 정수 형으로 변환
#PutTime.extend(PutTime_)
PutYear=int(input())
PutMonth=int(input())
PutDay=int(input())
PutHour=int(input())
PutMinute=int(input())
Time.append(datetime.datetime(PutYear,PutMonth,PutDay,PutHour,PutMinute))

PutName=input()#이름 입력
Name=[]
Name.append(PutName)

Importance=[]#중요도
PutImportance=input()
Importance.append(PutImportance)


