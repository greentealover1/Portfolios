#*a;a가 가리키는 변수의 시작 주소를 의미
list_b=[1,3,5,7,9]
a,*b,c=list_b
#*b이면, 일반 변수는 a,c는 일대일로 매칭되는데,*b하면,*b가 리스트 개수에 맟줘 동적으로 3,5,7의 주소를 가리켜서 3,5,6print
# print("b:",b)
# *a,b,c=list_b
# print("a:",a)
# a,*b,c=list_b
# print("b:",b)

def para_func(*para):
    result=0
    for num in para:
        result+=num
    return result
hap=0
hap=para_func(10,20)
print("매개변수가 2개인 함수를 호출한 결과==>%d"%hap)
hap=para_func(10,20,30,40)
print("매개변수 3개인 함수를 호출한 결과==>%d"%hap)