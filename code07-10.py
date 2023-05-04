# foods={"떡볶이":"오뎅","짜장면:":"단무지","라면":"김치","피자":"피클","맥주":"땅콩","치킨":"치킨무","삼겹살":"상추"}
# while True:
#     f=input("%s 중 좋아하는 음식은?"%(str(list(foods.keys()))))
#     if f in foods:
#         print("<%s>궁합 음식은 <%s>입니다."%(f,foods.get(f)))
#     elif f=="끝":
#         break
#     else:
#         print("그런 음식이 없어요.확인해보세요.")

score_dic={"kim":[98,83,95],"lee":[98,88,92]}
for name,scores in score_dic.items():
    #print(name,sum(scores)/len(scores))
    print(name,"평균:%5.1f"%(sum(scores)/len(scores)))#소수점 format맞춰서 출력
    print("이름:%s 수학 점수:%d 영어 점수:%d 국어점수:%d"%(name,scores[0],scores[1],scores[2]))


