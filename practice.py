# argv:*개수에 맞춰 동적으로 지정됨
# list_b=[1,3,5,7,9]
# a,*b,c=list_b
# print("b:",b)
# *a,b,c=list_b
# print("a:",a)
# a,*b=list_b
# print("b:",b)

# def para_func(v1,v2,v3=0):
#     result=0
#     result=v1+v2+v3
#     return result
# hap=0
# hap=para_func(10,20)
# print("hap:",hap)
# hap=para_func(10,20,30)
# print("hap:",hap)

# def hap(*para):
#     print("합계는 :",sum(para))
# hap(98,72.84)
# hap(92,95,89,76,54)

# def para_func(*para):
#     result=0
#     for num in para:
#         result+=num
#     return result
# hap=0
# hap=para_func(10,20)
# print("매개변수 2개의 합:", hap)
# hap=para_func(10,20,30)
# print("매개변수 3개의 합:", hap)

# def dic_func(**para):
#     for k in para.keys():
#         print("%s-->%d명입니다."%(k,para[k]))
# dic_func(트와이스=9,소녀시대=7,걸스데이=4,블랙핑크=4)
#
# def dic_func(**para):
#     for k in para.keys():
#         print("%s-->%s"%(k,para[k]))#key값,key에 해당하는 value값
# dic_func(김연아="피겨스케이팅",홍명보="축구",서태웅="농구")#키는 그냥 써도 되지만 밸류값은 문자열이면 ""기호 쓴다.

# def personal_info(name,age,address):
#     print("이름:",name)
#     print("나이:",age)
#     print("주소:",address)
#     #name변수로 넘겨받도록 선언해야 한다(즉 key값에 name,age,address변수가 있어야 함-매개변수-꼭 지킨다)
# #함수 호출시 key값에 맞춰서 value값이 들어간다.
# x={"name":"홍길동","age":30,"address":"서울시 용산구 이촌동"}
# personal_info(*x)#*x는 name,age,address라는 key값을 출력
# personal_info(**x)#**x:name,age,address key값에 맞는 value값이 들어간다.

# def food(style,menu,cost):
#     print("종류:",style)
#     print("메뉴:",menu)
#     print("가격:",cost)
# x={"style":"italian","menu":"egg benedict","cost":10000}
# food(*x)
# food(**x)