from high_low_arts import logo, vs
from higer_lower_data import data
import random


def format_data(account):
    accont_name = account['name']
    account_description = account['description']
    account_country = account['country']
    return f"{accont_name} - a {account_description} - from {account_country}"

def check_answer(user_guess,account_a,account_b):
    if account_a > account_b:
        return user_guess == "a"
    else:
        return user_guess == "b"

print(logo)
score=0
game_should_continue = True

account_b = random.choice(data)

while game_should_continue:
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A:{format_data(account_a)}")
    print(vs)
    print(f"Compare B:{format_data(account_b)}")

    guess = input("Who has more followers? Type 'A' or 'B':").lower()

    print("\n"*20)
    print(logo)

    a_follower_count = account_a['follower_count']
    b_follower_count = account_b['follower_count']
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    if is_correct:
        score += 1
        print(f"Correct! You got it in {a_follower_count} followers.")
        print(f"You have {score} score .")
    else:
        print(f"Wrong! Finel score {score}.")
        game_should_continue = False
