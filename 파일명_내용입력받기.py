fname=""
fname=input("파일명을 입력하세요:")
file=open("./"+fname,'w',encoding='UTF-8')
outstr=""
while True:
    outstr=input("내용 입력==>")
    if outstr!="":
        file.writelines(outstr+"\n")
    else:
        break
file.close()
print("%s파일 저장 완료"%fname)
instr=""
file=open("./%s"%fname,"r",encoding='UTF-8')
infile=file.readlines()
for instr in infile:
    if instr!="":
        print(instr,end="")
    else:
        break
file.close()
