#1번
'''num1=int(input("정수를 입력하시오:"))
num2=int(input("정수를 입력하시오:"))
if num1%num2==0:
    print("약수입니다.")
else:
    print("약수가 아닙니다.")'''

#2번
'''num=int(input("정수를 입력하시오:"))
if num>0:
    print("양수")
elif num==0:
    print("0")
else:
    print("음수")'''

#3번
'''word=input("문자를 입력하시오:")
if word=='R':
    print("Rectangle")
elif word=='r':
    print("Rectangle")
elif word=='T':
    print("Triangle")
elif word=='t':
    print("Triangle")
elif word=='C':
    print("Circle")
elif word=='c':
    print("Circle")
else:
    print("Unknown")'''

#4번
'''num1=int(input("첫 번째 정수를 입력하시오:"))
num2=int(input("두 번째 정수를 입력하시오:"))
num3=int(input("세 번째 정수를 입력하시오:"))
min_num=0
if num1>num2:
    if num2>num3:
        min_num=num3
    else:
        min_num=num2
else:#num2>num1
    if num1>num3:
        min_num=num3
    else:
        min_num=num1
print("제일 작은 정수는 %d입니다."%(min_num))'''

#5번
'''height=int(input("키를 입력하시오(cm):"))
age=int(input("나이를 입력하시오:"))
if height>=140:
    if age>=10:
        print("타도 좋습니다.")
else:
    print("죄송합니다.")'''

#6번
'''w=int(input("체중을 입력하시오(kg):"))
h=int(input("키를 입력하시오(cm):"))
weight=(h-100)*0.9
if w-weight>=10:
    print("과체중입니다.")
elif w-weight<=-10:
    print("저체중입니다.")
else:
    print("표준 체중입니다.")'''

        
        
