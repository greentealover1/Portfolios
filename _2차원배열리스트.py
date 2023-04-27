list1=[]
list2=[]
value=0
for i in range(5):
    for j in range(4):
        list1.append(value)
        value+=3
    list2.append(list1)
    list1=[]
for i in range(4):
    for j in range(5):
        print("%3d "%list2[j][i],end=" ")
    print()

