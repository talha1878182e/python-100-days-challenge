import random

Rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

Paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

Scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

game_list = [Rock, Paper, Scissors]

user_choose = int(input("What do you choose? Rock (0), Paper (1), Scissors (2): "))

if user_choose < 0 or user_choose >= 3:
    print("Oops! You typed an invalid number, you lose!")
else:
    print(game_list[user_choose])

    computer_choose = random.randint(0, 2)
    print("Computer Choose:")
    print(game_list[computer_choose])

    if user_choose == 0 and computer_choose == 2:
        print("You win!")
    elif computer_choose == 0 and user_choose == 2:
        print("You lose!")
    elif computer_choose > user_choose:
        print("You lose!")
    elif user_choose > computer_choose:
        print("You win!")
    elif computer_choose == user_choose:
        print("It's a draw!")
