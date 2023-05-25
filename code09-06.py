outfile=None
outstr=""
outfile=open('./mydata3','w',encoding='UTF-8')
while True:
    outstr=input("내용입력==>")#사용자가 입력하면
    if outstr!="":#해당파일에 한행씩 쓰기
        outfile.writelines(outstr+"\n")
    else:#입력한 내용 없으면 break
        break
outfile.close()
print("mydata3파일이 저장됨")
