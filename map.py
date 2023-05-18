#a=[1.2,2.5,3.7,4.6]
# for i in range(len(a)):
#     a[i]=int(a[i])
# print(a)
#map:리스트로부터 원소를 하나씩 꺼내서 함수를 적용시킨 다음, 그 결과를 새로운 리스트로 생성
#a=list(map(int,a))#map(함수,리스트):함수와 리스트를 인자 사용
#print(a)

# mylist=[1,2,3,4,5]
# def add10(num):
#     return num+10
# for i in range(len(mylist)):
#     mylist[i]=add10(mylist[i])
# print(mylist)

# mylist=[1,2,3,4,5]
# add10=lambda num:num+10
# mylist=list(map(add10,mylist))
# print(mylist)

# mylist=[1,2,3,4,5]
# mylist=list(map(lambda num:num+10,mylist))
# print(mylist)

# list1=[1,2,3,4]
# list2=[10,20,30,40]
# haplist=list(map(lambda n1,n2:n1+n2,list1,list2))
# print(haplist)
#
# a=(1,2,3,4,)#내가 만든 예제
# b=(100,200,300,400,)
# sum_s=tuple(map(lambda n1,n2:n1*n2,a,b))
# print(sum_s)

