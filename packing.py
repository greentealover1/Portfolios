#packing:개별 변수값을 list또는 tuple로 만드는 것
#unpacking:tuple,list데이터 타입을 "="명령어를 통해 개별 변수값으로 지정하는 것
# list_a=[1,3,9,87]
# a,b,c,d=list_a
# print(d,c,b,a)

#매개변수의개수를 지정하지 않고 전달하는 방법
# def personal_info(a,age,address):#매개변수와 딕셔너리 키값을 일치시키면 사용 가능!
#     print("이름:",a)
#     print("나이:",age)
#     print("주소:",address)
# x={"a":"홍길동","age":30,"address":"서울시 용산구 이촌동"}
#personal_info(*x)
#personal_info(**x)

#함수 호출할때 딕셔너리 형식의 매개변수를 키=value값 형식으로 사용(키는 문자열)
#매개변수의 개수를 지정하지 않고 전달하는 방법:함수(**딕셔너리)
#*매개변수:튜플 형태로 처리
#**매개변수:딕셔너리 형태로 처리
def dic_func(**para):
    for k in para.keys():
        print("%s-->%d명입니다."%(k,para[k]))
dic_func(트와이스=9,소녀시대=7,걸스데이=4,블랙핑크=4)
#dic_func(김연아="피겨스케이팅",홍명보="축구",현주엽="농구")





