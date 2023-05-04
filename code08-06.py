#반환값이 없는 함수
#함수를 실행한 결과, 돌려줄 것이 없는 경우에는 return문을 생략
#반환값이 없이 return문만 써도 된다->자주 쓰이는 형식
#반환값 없이 함수를 마치면 아무것도 반환하지 않고 함수가 종료됨
# def func1():
#     print("반환값이 없는 함수 실행")
# func1()

#값 반환 함수
def func2():
    result=100
    return result
hap=func2()
print("func2()에서 돌려준 값==>",hap)

def func3():
    result1=100
    result2=200
    return result1,result2
hap1,hap2=0,0
hap1,hap2=func3()
print("func3()에서 돌려준 값==>",hap1,hap2)

