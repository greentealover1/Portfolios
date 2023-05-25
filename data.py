#data={x:3*x**2-5 for x in range(10)}#dictionary comprehension
# data={}
# for x in range(10):
#     data[x]=3*x**2-5
# with open("./data","w") as f:
#     for x,y in data.items():
#         f.writelines(str(x)+" "+str(y)+"\n")
# with open('./data','r') as f:
#     lines=f.readlines()
# for instr in lines:
#     print(instr,end=" ")

# data={}
# for x in range(10):
#     data[x]=3*x**2-5
# with open("./data","w") as f:
#     for x,y in data.items():
#         f.writelines(str(x)+" "+str(y)+"\n")
# with open("./data","r") as f:
#     for i in f.readlines():
#         print(i,end=" ")
# f.close()

with open('./test','r') as f:
    s=f.read()
    elems=[float(x) for x in s.split(',')]#split:()안에 있는 문자기준으로 구분해서 데이터 가져옴
    print("총합:%f"%(sum(elems)))
    for v in elems:
        print(v)
