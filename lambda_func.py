# def outfunc(v1,v2):
#     def infunc(num1,num2):
#         return num1+num2
#     return infunc(v1,v2)
# print(outfunc(10,20))#outfunc안에 infunc함수가 있으므로 함수밖에서 호출하면 오류 발생

def hap(num1,num2):
    res=num1+num2
    return res
print(hap(10,20))
hap2=lambda num1,num2:num1+num2
print(hap2(10,20))
hap3=lambda num1=10,num2=20:num1+num2
print(hap3())
print(hap3(100,200))

