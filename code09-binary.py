# infp,outfp=None,None
# instr=""
# infp=open('C:/Windows/notepad.exe','rb')
# outfp=open('C:/Temp/notepad.exe','wb')
# while True:
#     instr=infp.read(1)#파일의 끝까지 한 바이트 씩 읽어와서 한바이트씩 파일에 쓰기
#     if not instr:
#         break
#     outfp.write(instr)
# infp.close()
# outfp.close()
# print('--이진 파일이 정상적으로 복사되었음--')
#아마 이진파일 내용은 딱히 쓸 수 있는 내용이 없어서 안나오거나 나온다고 해도 이론문제로만 나올듯
# import shutil
# print(dir(shutil))#파일 디렉토리 다루기:shutil,os모듈,os.path모듈:파일,디렉토리 폴더 다룰 수 있는 다양한 함수

# import os
# print(dir(os))

# import os.path
# print(os.path)

#파일 디렉토리 복사
# import shutil#shutil.copy(소스파일,타겟파일) 함수 사용
# shutil.copy('C:/Windows/notepad.exe','C:/Temp/mynote.exe')
#디렉토리 생성/삭제:os.mkdir(폴더명)함수사용,shutil.rmtree(폴더명)함수 사용
import os
import shutil
os.mkdir('C:/mydir/')
os.mkdir('C:/mydir/dir1')
# shutil.rmtree('C:/mydir/')

