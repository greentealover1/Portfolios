import random

# 카드 리스트 초기화
cards = [11, 11, 11, 11, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8,
         9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]

# 무작위로 덱을 섞기
random.shuffle(cards)

# 무작위로 카드 선택하고 제거
def draw_cards(deck, num=2):
    drawn_cards = deck[:num]
    del deck[:num]
    return drawn_cards

# 점수 계산 함수
def score_sum(cards):
    value = sum(cards)
    ace_count = cards.count(11)
    while value > 21 and ace_count:
        value -= 10
        ace_count -= 1
    return value

# 승자 판정 함수
def winner(my_score, dealer_score):
    if my_score == 21 and dealer_score != 21:
        print("Blackjack! You Win!")
    elif dealer_score == 21 and my_score != 21:
        print("Blackjack! Dealer Wins!")
    elif my_score > 21:
        print("Lose (You Busted)")
    elif dealer_score > 21:
        print("Win (Dealer Busted)")
    elif my_score > dealer_score:
        print("Win")
    elif my_score == dealer_score:
        print("Draw")
    else:
        print("Lose")

# 게임 시작
def choose():
    my_pick = draw_cards(cards, 2)
    dealer_pick = draw_cards(cards, 2)

    print("나:", my_pick)
    print("딜러: [", dealer_pick[0], ", ? ]")
    print("덱 상태:", cards)

    my_score = score_sum(my_pick)
    dealer_score = score_sum(dealer_pick)

    print("(me)현재 점수:", my_score)
    game_continue = True

    # 플레이어가 블랙잭일 경우
    if my_score == 21:
        game_continue = False
        winner(my_score, dealer_score)
        return

    while game_continue:
        # 플레이어의 차례
        print(f"현재 덱 상태: {cards}")

        stand_hit = input("stand or hit? ")
        if stand_hit == "stand":
            break
        elif stand_hit == "hit":
            new_card = draw_cards(cards, 1)
            my_pick.extend(new_card)
            my_score = score_sum(my_pick)
            print("현재 내가 보유한 카드들:", my_pick)
            print("나의 점수:", my_score)
            if my_score == 21:
                game_continue = False
                winner(my_score, dealer_score)
                return
            elif my_score > 21:
                game_continue = False
            # 딜러의 차례
            if dealer_score < 17:
                new_card = draw_cards(cards, 1)
                dealer_pick.extend(new_card)
                dealer_score = score_sum(dealer_pick)
                print("딜러가 뽑은 새 카드들:", dealer_pick)
                if dealer_score == 21 or dealer_score > 21:
                    game_continue = False

    # 딜러의 차례가 이어짐
    while dealer_score < 17 and game_continue:
        new_card = draw_cards(cards, 1)
        dealer_pick.extend(new_card)
        dealer_score = score_sum(dealer_pick)
        print("딜러가 뽑은 새 카드들:", dealer_pick)
        if dealer_score == 21 or dealer_score > 21:
            game_continue = False

    # 게임이 끝나면 딜러의 모든 카드를 공개
    print("딜러의 최종 카드들:", dealer_pick)
    print("딜러의 최종 점수:", dealer_score)
    winner(my_score, dealer_score)

choose()
