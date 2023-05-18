file=None
instr,fname="",""
inlist=[]
fname=input("파일명을 입력하세요:")
file=open(fname,"r",encoding='UTF-8')#반드시 encoding='UTF-8'를 해야함
inlist=file.readlines()
for instr in inlist:
    print(instr,end="")
file.close()
