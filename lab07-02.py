print("홍길동 선수 경기 끝났습니다.~~짝짝짝")
rate=[]
for i in range(5):
    rate.append(0)
sum=0
for i in range(5):
    score=int(input("평가점수==>"))
    sum += score
    rate.append(score)
print("심사위원 평균 점수:",sum/5)