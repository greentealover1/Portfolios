import random#가위바위보 게임
toss=[]
for i in range(10000):
    coma=random.choice(["가위","바위","보"])
    comb=random.choice(['가위','바위','보'])
    if coma=="가위":
        if comb=="보":
            toss.append("A")
        elif comb=="바위":
            toss.append("B")
        else:
            toss.append("없음")
    elif coma=="바위":
        if comb=="가위":
            toss.append("A")
        elif comb=="보":
            toss.append("B")
        else:
            toss.append("없음")
    else:#보
        if comb=="바위":
            toss.append("A")
        elif comb=="가위":
            toss.append("B")
        else:
            toss.append("없음")
print("10000번 중 컴퓨터A의 승리:",toss.count("A"))
print("10000번 중 컴퓨터B의 승리:",toss.count("B"))
print("10000번 중 비긴 경기:",toss.count("없음"))