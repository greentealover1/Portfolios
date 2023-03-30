##score=int(input("점수를 입력:"))
##if score>=90:
##    print("A",end="")
##elif score>=80:
##    print("B",end="")
##elif score>=70:
##    print("C",end="")
##elif score>=60:
##    print("D",end="")
##else:
##    print("F",end="")
##print("학점입니다.")

'''
score=65
res=''
if score>=60:
    res="합격"
else:
    res="불합격"
print(res)'''

score=int(input("점수 입력:"))
res='합격' if score>=60 else '불합격' #삼항연산자
print(res)
