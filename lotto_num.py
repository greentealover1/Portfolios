# import random
# def getnumber():
#     return random.randrange(1,46)
# lotto=[]
# num=0
# print("** 로또 추첨을 시작합니다. **\n")
# while True:
#     num=getnumber()
#     if lotto.count(num)==0:
#         lotto.append(num)
#     if len(lotto)>=6:
#         break
# print("추첨된 로또 번호==>",end="")
# lotto.sort()
# for i in range(0,6):
#     print("%d "%lotto[i],end="")

#값에 의한 전달:일반 변수나 값을 전달할때 함수에 동일한 크기의 별도의 공간이 확보되어 값이 전달됨
#참조에 의한 전달:리스트(튜플,딕셔너리 등)를 매개변수로 전달하는 경우, 주소가 전달되어 메모리 공간이 공유
def func(p):
    p[0]=222
v=[111]
func(v)
print(v[0])#지역변수값을 우선해서 값 전달
