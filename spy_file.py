securefile=None
instr,secure="",""
securefile=open("./secure.txt","w",encoding='UTF-8')
while True:
    instr=input("스파이에게 전달할 메세지==>")
    if instr=="":
        break
    for ch in instr:
        num=ord(ch)
        num+=100
        secure+=chr(num)
securefile.writelines(secure)
securefile.close()
print('secure.txt 암호화 완료')
