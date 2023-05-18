#readlines():파일의 내용을 한꺼번에 읽어와서 리스트에 저장
file=None
mlist=[]
file=open(r"C:\Users\Sungshin\PycharmProjects\weel12_file\file","r",encoding='UTF-8')
mlist=file.readlines()
print(mlist)
file.close()