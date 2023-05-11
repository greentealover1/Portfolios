#global예약어:함수안에서 사용되는 변수!
#지역변수 대신에 무조건 전역변수로 사용하고 싶은 경우에 사용
#globacl예약어와 함꼐 나오는 변수명은 무조건 전역변수임
def func1():
    global a
    a=10
    print("func1()에서 a의 값:",a)
def func2():
    print("func2()에서 a의 값:",a)
a=20
func1()#10 전역변수인 a=20이 있어도 func함수에 a의 값을  global전역변수 10으로 설정
func2()#10
#datetime:날짜와 시간을 함께 저장하는 클래스
#date:날짜만 저장하는 클래스
#time:시간만 저장하는 클래스
#timedelta:시간 구간 정보를 저장하는 클래스
