animals={"개":"강아지","호랑이":"개호주","곰":"능소니","말":"망아지","닭":"병아리","고등어":"고도리","명태":"노가리"};
while True:
    baby=input("%s중 새끼 이름을 알고 싶은 동물은?"%(str(list(animals.keys()))))
    if baby in animals:
        print("<%s>의 새끼는 <%s>입니다."%(baby,animals[baby]))
    elif baby=="끝":
        break
    else:
        print("그런 동물 없어요")
