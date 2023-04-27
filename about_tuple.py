#읽기전용의 리스트
#튜플은 소괄호 ()사용, 값 수정 불가, 읽기전용 데이터->index사용 가능 but 인덱스를 통해 값을 변경 불가
# numTup1=(10,20,30)
# print(numTup1)
# numTup2=10,20,30
# print(numTup2)
# numTup3=10,
# print(numTup3)#튜플 형식
# numTup4=10
# print(numTup4)#그냥 int형 변수

# numTup1=(10,20,30)#튜플 삭제
# del(numTup1)

numTup1=(10,20,30,40)
# print(numTup1[0])
# print(numTup1[0]+numTup1[1]+numTup1[2])

# numTup2=('A','B')
# print(numTup1+numTup2)
# print(numTup2*3)#58

#2차원 tuple
# tt=((1,2,3),(4,5,6),(7,8,9))
# for i in range(3):
#     for j in range(3):
#         print("%3d"%(tt[i][j]),end=' ')
#     print()

#튜풀->리스트->튜플로 상호교환
myTuple=(10,20,30)
myList=list(myTuple)
myList.append(40)
myTuple=tuple(myList)
print(myTuple)