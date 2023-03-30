money=int(input("숫자 입력:"))
c1000=money//1000#1000원 몫
money=money%1000#1000원 나머지
print("천원짜리:",c1000)
c100=money//100
money=money%100
print("백원짜리:",c100)
c10=money//10
money=money%10
print("십원짜리:",c10)
print("일원짜리:",money)
