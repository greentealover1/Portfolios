#pass :함수의 이름과 형태만 만들고 나중에 코딩할 때 사용 하는 키워트
#그외 용도: if문이나 반복문에서 아무것도 안하는 코드로 채울 때도 사용 가능

import random
# def lottofunc():
#     lotto=random.randint(1,45)
#     return lotto
# lottolist=[]
# num=0
# while True:
#     num=lottofunc()
#     if num in lottolist:
#         continue
#     else:
#         lottolist.append(num)
#     if len(lottolist)==6:
#         break
# print(" **로또 추첨을 시작합니다.** ")
# lottolist.sort()
# print("오늘의 로또 번호==>",end='')
# for i in range(0,6):
#     print(lottolist[i]," ",end="")

def lottofunc():
    lotto=random.randint(1,45)
    return lotto
lottolist=[]
while True:
    num=lottofunc()
    if num in lottolist:
        continue
    else:
        lottolist.append(num)
    if len(lottolist)==6:
        break
print(" **로또 추첨을 시작합니다.** ")
lottolist.sort()
print("오늘의 로또 번호==>",end="")
for i in lottolist:
    print(i,end=" ")