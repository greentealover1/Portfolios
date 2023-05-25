#반복문으로 문자열 여러 줄을 파일에 쓰기
# with open('./myname','w') as file:
#     for i in range(3):
#         file.writelines("Hello world\n")
# with open('./myname','w') as file:
#     for i in range(3):
#         file.writelines("Hello python\n")

#리스트에 들어있는 문자열을 파일에 쓰기
# lines=["안녕하세요\n","파이썬\n","코딩도장입니다.\n"]
# with open('./myname','w',encoding='UTF-8') as f:
#     f.writelines(lines)

#파일의 내용을 한줄씩 리스트에 가져오기->readlines를 하면, 리스트형태로 파일 내용 가져오기
# with open('./python_hello','r',encoding='UTF-8') as file:
#     lines=file.readlines()
#     print(lines)

#파일의 내용을 한 줄씩 순차적으로 읽어오기
# with open('./python_hello','r',encoding='UTF-8') as file:
#     for i in file:
#         print(i.strip('\n'))
with open('./python_hello','r',encoding='UTF-8') as f:
    line=None
    while line!="":
        line=f.readline()
        print(line.strip("\n"))