file=None
instr=""
file=open(r"C:\Users\Sungshin\PycharmProjects\weel12_file\file","r",encoding='UTF-8')
while True:
    instr=file.readline()
    if instr=="":
        break
    print(instr,end="")
file.close()

#arrangement
file=None
instr=""
file=open(r"C:\Users\Sungshin\PycharmProjects\weel12_file\file","r",encoding='UTF-8')
num=0
while True:
    instr=file.readline()
    if instr=="":
        break
    num+=1
    print("%d: %s"%(num,instr),end="")
file.close()

