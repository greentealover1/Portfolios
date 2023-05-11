#datetime:날짜와 시간을 함께 저장하는 클래스
#date:날짜만 저장하는 클래스
#time:시간만 저장하는 클래스
#timedelta:시간 구간 정보를 저장하는 클래스
#100일 기념일 날짜 구하기
#from datetime import datetime,timedelta
import datetime
def getcurrent():#현재날짜를 구해서 반환하는 함수 만들기
    curdate=datetime.now()
    return curdate
def getafterdate(now,day):#전달받은 날짜로부터 지정일자 후의 날짜를 구해서 반환하는 함수 만들기
    retdate=now+timedelta(days=day)
    return retdate
nowdate=getcurrent()
print("현재 날짜와 시간==>",nowdate)
afterdate=getafterdate(nowdate,100)
print("100일 후 날짜와 시간==>",afterdate)

