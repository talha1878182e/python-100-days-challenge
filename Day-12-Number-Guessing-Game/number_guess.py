import random
import time
import number_arts
print(number_arts.welcome)
time.sleep(0.5)
print(number_arts.to)
time.sleep(0.5)
print(number_arts.gnumber)
time.sleep(0.5)


random_number=random.randint(1,100)
print("Sayı seçiliyor.......")
time.sleep(1)
print(f"Seçilen sayı : {random_number}")

attempts = 0

difficulty = input("Choose a difficulty. Type 'easy' ,'medium' or 'hard' :").lower()
if difficulty == "easy":
    attempts = 10
elif difficulty == "medium":
    attempts = 5
elif difficulty == "hard":
    attempts = 3
else:
    attempts = 10
print(f"You have {attempts} attempts remaining to guess the number.")
game_is_over = False
while not game_is_over:
    guess_number = int(input("Make a guess:"))
    attempts -= 1
    if guess_number == random_number:
        print(f"You got it! The answer was {random_number}.")
        game_is_over = True
    elif attempts == 0:
        print(f" You've run out of guesses, you lose! The number was {random_number}.")
        game_is_over = True
    elif guess_number > random_number:
        print("Guess too high")
        print(f"You have {attempts} attempts remaining.")
    elif guess_number < random_number:
        print("Guess too low")
        print(f"You have {attempts} attempts remaining.")

