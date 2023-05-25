infile,outfile=None,None
instr=""
infile=open('./mydata2','r',encoding='UTF-8')
outfile=open('./mydata3','w',encoding='UTF-8')
inlist=infile.readlines()
for instr in inlist:
    outfile.writelines(instr)
infile.close()
outfile.close()
print('mydata2.txt내용이 mydata.txt로 복사됨')