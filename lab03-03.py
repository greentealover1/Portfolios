python=3
mobile=2
excel=1
A=4.5
A0=4.0
B=3.5
avg=((python*B)+(mobile*A0)+(excel*A))/(python+mobile+excel)
#평균:학점 합계/학점의 수
print("평균 학점:",avg)
print("%7.2f"%(avg))
print("평균 학점:","%7.2f"%avg)#일곱자리 확보후 소수점아래둘째자리까지 표시
