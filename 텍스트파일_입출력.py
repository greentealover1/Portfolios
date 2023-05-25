infp,outfp=None,None
instr,outstr="",""
i=0
secu=0
choice=input("1.암호화 2.암호해석 중 선택:")
infname=input("입력 파일명을 입력하세요:")
outfname=input("출력 파일명을 입력하세요:")
if choice=='1':
    secu=100#100만큼 ord숫자 더하기(암호화)
elif choice=='2':
    secu=-100#복호화(암호화 과정에서 100더한 것을 빼줌)
infp=open(infname,'r',encoding='UTF-8')
outfp=open(outfname,'w',encoding='UTF-8')
while True:#infname파일의 끝까지 읽어온다.
    instr=infp.readline()#instr에 읽어온 것이 없다면 while문을 빠져나간다
    if not instr:
        break
    outstr=""#출력문
    for i in range(0,len(instr)):#instr내용을 리스트로 만들고
        ch=instr[i]#그 문자리스트의 ord(아스키코드)값을 chnum에 저장
        chnum=ord(ch)
        chnum=chnum+secu##암호화할때 choice=1일때는 -100만큼 빼고 choice=2일때는 100만큼
        ch2=chr(chnum)#암호화한 문자들을 ch2변수에 저장
        outstr=outstr+ch2#outstr에 ch2암호화한 내용 저장 & 복호화할때도 그 해당 새 파일에 내용 저장
    outfp.write(outstr)#파일 내용 적기
outfp.close()
infp.close()
print("%s-->%s 변환완료"%(infname,outfname))
