file=None
mlist=[]
instr=""
file=open(r"C:\Users\Sungshin\PycharmProjects\weel12_file\file","r",encoding="UTF-8")
mlist=file.readlines()
for instr in mlist:
    print(instr,end="")
file.close()