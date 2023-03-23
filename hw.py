'''
num=int(input("과자의 개수:"))
count=int(input("한 사람당 나누어주는 과자의 개수:"))

num=52
count=3
print("과자의 개수:",num)
print("한 사람당 나누어주는 과자의 개수:",count)

people=num//count#인원
num=num%count
print("최대 %d명에게 나누어줄 수 있습니다."%(people))
print("남는 과자는 %d개입니다."%(num))
'''

'''
side1=int(input("삼각형 첫 번째 변의 길이:"))
side2=int(input("삼각형 두 번째 변의 길이:"))
side3=(side1+side2)-1
print("삼각형의 나머지 변의 최대 길이:%d"%side3)
'''

'''
time=int(input("시간을 입력하세요:"))
minute=int(input("분을 입력하세요:"))
total_second=(60*time+minute)*60
print("%d시간 %d분은 %d초입니다."%(time,minute,total_second))
'''

'''
x=int(input("x의 값을 입력하세요:"))
y=int(input("y의 값을 입력하세요:"))
val=(x+y)**2
print("(%d+%d)^2=%d"%(x,y,val))
'''
