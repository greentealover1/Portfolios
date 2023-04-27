# numlist = [10, 20, 30, 40, 50, 60, 70]
# print(numlist[0])
# print(numlist[0:3])
# print(numlist[:3])
# print(numlist[2:])
# print(numlist[2:4])
# print(numlist[-1])
# print(numlist[-2])
# print(numlist[::2])
# print(numlist[::-2])
# print(numlist[::-1])
# print(numlist)

#리스트 값 변경하기
# numList = [10, 20, 30]
# numList[1:3] = [200, 201]#인덱스 1,2번이 각각 200,201로 변경된다.
# print(numList)

#리스트 값 추가하기
# numList = [10, 20, 30]
# numList.append(50)
# print(numList)
# numList.insert(1,7)#insert(인덱스,요소)
# print(numList)

# numlist=['orange','banana','watermelon']
# numlist.sort()
# print(numlist)

#del:리스트 항목 삭제->특히 리스트 이름을 넣으면 리스트가 통째로 삭제된다.
# numList=[10,20,30]#
# del(numList[1])#리스트 자체 지울때는 del이용하고 특정 인덱스 지울때도 사용가능
# print(numList)

# numList=[10,20,30,10,10]#remove:특정 요소를 삭제할때 val값을 매개변수로 넣어서 삭제한다.
# numList.remove(10)#중복된 값이 있으면,가장 처음으로 발견되는 요소10을 삭제해줌
# print(numList)

# numList=[10,20,30]
# numList.pop()#마지막 인덱스 위치의 값을 삭제해서 반환
# print(numList)

# numList=[10,20,30,10,10]
# print(numList.count(10))

# numList=[20,10,40,50,30]
# numList.sort()#오름차순 정렬
# print(numList)
# numList.sort(reverse=True)
# print(numList)

#numList=[20,10,40,50,30]
# numList.reverse()#리스트의 요소 순서 거꾸로
# print(numList)

# numList=[10,20,30] ##리스트를 새로운 리스트로 복사한다.
# numList2=numList.copy()
# print(numList2)

#리스트 함축
# squares=[x*x for x in range(10)]
# print(squares)
# squares=[x*x for x in range(10) if x%2==0]#짝수 x값들에 대해서만 x*x출력
# print(squares)

#한줄for문 조건연산자
# words=["All","good","things","must","come","to","an","end"]
# letters=[w[0] for w in words]
# print(letters)

# numbers=[x+y for x in ['a','b','c'] for y in ['x','y','z']]
# print(numbers)

#0-99까지 정수 중에서 2의 배수이고 동시에 3의 배수인 수들을 모아서 리스트 함축을 사용해서 리스트로 만들기
# numbers=[i for i in range(0,100) if i%2==0 and i%3==0]
# print(numbers)



