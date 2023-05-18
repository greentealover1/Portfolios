import os
infp=None
fname,inlist,instr="",[],""
fname=input("파일명을 입력하세요:")
if os.path.exists(fname):
    infp=open(fname,"r")
    inlist=infp.readlines()
    for instr in inlist:
        print(instr,end="")
    infp.close()
else:
    print("%s 라는 파일이 없습니다."%fname)