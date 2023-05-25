file=None
instr,fname="",""
flist=[]
fname=input("파일명을 입력하세요:")
#file=open(fname,"r",encoding='UTF-8')#utf8로 해줘야 해당 파일 내용을 불러올 수 있음
file=open(fname,'r')
flist=file.readlines()
for instr in flist:
    print(instr,end="")#\n이 기본 flist즉 읽은 내용에 있으니까 없애주는 역할 수행
file.close()