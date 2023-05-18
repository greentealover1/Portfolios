#재귀함수:자기 자신을 호출하는 함수
# def factorial(n):
#     if n<=0:
#         return 1
#     else:
#         return n*factorial(n-1)
# s=factorial(4)
# print(s)

# def count(num):
#     if num>=1:
#         print(num,end=' ')
#         count(num-1)
#     else:
#         return
# count(10)
# print()
# count(20)

# def genfunc():#yield:함수를 종결하지 않으면서 값을 계속 반환
#     yield 1
#     yield 2
#     yield 3
# print(list(genfunc()))

def genfunc(num):#yield문으로 값을 반환한 후 계속 진행
    for i in range(0,num):
        yield i
        print("제너레이터 진행 중")

for data in genfunc(5):
    print(data)



