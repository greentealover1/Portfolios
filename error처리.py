import os
infp=None#값이 존재하지 않는 경우
fname,inlist,instr="",[],''
fname=input("파일명을 입력하세요:")
if os.path.exists(fname):#os.path.exists:는 boolean값을 반환해서 true,false를 반환한다.
    infp=open(fname,'r')
    inlist=infp.readlines()
    for instr in inlist:
        print(instr,end="")
    infp.close()
else:
    print("%s파일이 없습니다."%fname)