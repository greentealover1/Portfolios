score=int(input("점수를 입력==>"))
if score>=90:
    print("A",end="")#end=""한줄로 출력하게 하기
else:
    if score>=80:
        print("B",end="")
    else:
        if score>=70:
            print("C",end="")
        else:
            if score>=60:
                print("D",end="")
            else:
                print("F",end="")
print("학점입니다.")
