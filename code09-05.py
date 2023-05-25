outfile=None
outstr=""
outfile=open('mydata2', 'w', encoding='UTF-8')
outstr="안녕하세요?"
outfile.writelines(outstr+"\n")
outstr="반갑습니다\n"
outfile.writelines(outstr)
outstr="자주 만나요^^"+"\n"
outfile.writelines(outstr)
print("myname.txt파일이 저장됨")