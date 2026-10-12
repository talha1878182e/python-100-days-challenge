import random
import black_jack_arts
import time


def deal_card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card= random.choice(cards)
    return card


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(u_score,c_score):
    if u_score == c_score:
        time.sleep(1)
        return black_jack_arts.draw
    elif c_score == 0:
        time.sleep(1)
        return black_jack_arts.lose
    elif u_score == 0:
        time.sleep(1)
        return black_jack_arts.black_jack
    elif u_score > 21:
        time.sleep(1)
        return black_jack_arts.lose
    elif c_score > 21:
        time.sleep(1)
        return black_jack_arts.win
    elif u_score > c_score:
        time.sleep(1)
        return black_jack_arts.win
    else:
        time.sleep(1)
        return black_jack_arts.lose


def blackjack_game():
    print(black_jack_arts.logo)

    user_cards = []
    computer_cards = []
    user_score = -1
    computer_score = -1
    is_game_over = False


    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    while not is_game_over:
        user_score= calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        time.sleep(1)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        time.sleep(1)
        print(f"Computer first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            time.sleep(1)
            user_should_deal = input("Do you want to deal another card? (y/n): ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    time.sleep(1)
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    time.sleep(1)
    print(f"Computer final hand: {computer_cards}, final score: {computer_score}")
    time.sleep(1)
    print(compare(user_score,computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n' \n=> ") == "y":
    print("\n"*20)
    blackjack_game()
    time.sleep(1)
