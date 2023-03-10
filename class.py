# #일반 유닛
# from random import*
# class Unit:#멤버변수:self.hp,self.name등 클래스안에서 정의된 멤버변수
#     def __init__(self,name,hp,speed):
#         self.name=name
#         self.hp=hp
#         self.speed=speed
#         print("{0}유닛이 생성되었습니다.".format(name))
#     def move(self,location):
#         print("[지상 유닛 이동]")
#         print("{0}:{1}방향으로 이동합니다. [속도{2}]"\
#             .format(self.name,location,self.speed))
#     def damaged(self,damage):
#         print("{0}:{1} 데미지를 입었습니다.".format(self.name,damage))
#         self.hp-=damage
#         print("{0}: 현재 체력은 {1} 입니다.".format(self.name,self.hp))
#         if self.hp<=0:
#             print("{0}: 파괴되었습니다".format(self.name)) 
# #공격 유닛
# class AttackUnit(Unit):#Attack unit이 Unit을 상속받는다는 것
#     def __init__(self,name,hp,speed,damage):
#         Unit.__init__(self,name,hp,speed)#상속받은 클래스의 멤버변수(명시하기)
#         self.damage=damage
#     def attack(self,location):
#         print("{0}:{1} 방향으로 적군을 공격합니다.[공격력 {2}"\
#             .format(self.name,location,self.damage))
#     def damaged(self,damage):
#         print("{0}:{1} 데미지를 입었습니다.".format(self.name,damage))

# #마린
# class Marine(AttackUnit):
#     def __init__(self):
#         AttackUnit.__init__(self,"마린",40,1,5)
#     #스팀팩
#     def stimpack(self):
#         if self.hp>10:
#             self.hp-=10
#             print("{0}:스팀팩을 사용합니다 (HP 10감소)".format(self.name))
#         else:
#             print("{0}:체력이 부족하여 스팀팩을 사용하지 않습니다.".format(self.name))
# class Tank(AttackUnit):
#     seize_devoloped=False#시즈모드 개발여부
#     def __init__(self):
#         AttackUnit.__init__(self,"탱크",150,1,35)
#         self.seize_mode=False
#     def set_seize_mode(self):
#         if Tank.seize_devoloped==False:
#             return
#         #현재 시즈모드가 아닐때->시즈모드
#         if self.seize_devoloped==False:
#             print("{0}:시즈모드로 전환합니다".format(self.name))
#             self.damage*=2
#             self.seize_mode=True
#         #현재 시즈모드일때->시즈모드해제
#         else:
#             print("{0}:시즈모드를 해제합니다.".format(self.name))
#             self.damage/=2
#             self.seize_mode=False
# #super기능:Unit.__init__(self) 와 Flyable.__init__(self)를 한번에 작성가능(생성자 초기화)
# class Flyable:
#     def __init__(self,flying_speed):
#         self.flying_speed=flying_speed
#     def fly(self,name,location):
#         print("{0}:{1}방향으로 날아갑니다 [속도{2}]"\
#             .format(name,location,self.flying_speed))
# #공중 공격 유닛
# class FlyableAttackUnit(AttackUnit,Flyable):
#     def __init__(self,name,hp,damage,flying_speed):
#         AttackUnit.__init__(self,name,hp,0,damage) #지상 스피드0
#         Flyable.__init__(self,flying_speed)
#     def move(self,location):
#         self.fly(self.name,location)
# class Wraith(FlyableAttackUnit):
#     def __init__(self):
#         FlyableAttackUnit.__init__(self,"레이스",80,20,5)
#         self.clocked=False #클로킹모드(해제 상태)
#     def clocking(self):
#         if self.clocked==True:#클로킹 모드->모드 해제
#             print("{0}:클로킹 모드 해제합니다.".format(self.name))
#             self.clocked=False
#         else:
#             print("{0}:클로킹 모드 설정합니다.".format(self.name))
#             self.clocked=True
# def game_start():
#     print("[알림] 새로운 게임을 시작합니다.")
# def game_over():
#     print("Playe :gg")
#     print("[Player]님이 게임에서 퇴장하셨습니다.")
# #게임 진행
# game_start()
# m1=Marine()
# m2=Marine()
# m3=Marine()
# t1=Tank()
# t2=Tank()
# w1=Wraith()
# attack_Units=[]
# attack_Units.append(m1)
# attack_Units.append(m2)
# attack_Units.append(m3)
# attack_Units.append(t1)
# attack_Units.append(t2)
# attack_Units.append(w1)
# #이동시키기
# for unit in attack_Units:
#     unit.move("1시")
# #탱크 시즈모드 개발
# Tank.seize_developed=True
# print("[알림] 탱크 시즈모드 개발이 완료되었습니다.")
# #공격모드준비(탱크:시즈모드,레이스:클로킹 ,마린:스팀팩)
# for unit in attack_Units:
#     if isinstance(unit,Marine):#특정 클래스의 인스턴스멤버인지 확인
#         unit.stimpack()
#     elif isinstance(unit,Tank):
#         unit.set_seize_mode()
#     elif isinstance(unit,Wraith):
#         unit.clocking()
# #전군 공격
# for unit in attack_Units:
#     unit.attack("1시")
# #전군 피해규모
# for unit in attack_Units:
#     unit.damaged(randint(5,21))
# #게임종료
# game_over()

class House:
    def __init__(self,location,house_type,deal_type,price,completion_year):
        self.location=location
        self.house_type=house_type
        self.deal_type=deal_type
        self.price=price
        self.completion_year=completion_year
    def show_detail(self):
        print(self.location,self.house_type,self.deal_type,self.price,self.completion_year)
houses=[]
house1=House("강남","아파트","매매","10억","2010년")
house2=House("마포","오피스텔","전세","5억","2007년")
house3=House("송파","빌라","월세","500/50","2000년")
houses.append(house1)
houses.append(house2)
houses.append(house3)
print("총 {0}대의 매물이 있습니다.".format(len(houses)))
for house in houses:
    house.show_detail()


