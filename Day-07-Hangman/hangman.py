import random
import time
import wordsss


print(wordsss.welcome)
time.sleep(1)
print(wordsss.to)
time.sleep(1)
print(wordsss.game)
lives = 6

random_words = random.choice(wordsss.words)
print(random_words)
place=""
time.sleep(1)
for position in range(len(random_words)):
    place +="_"
print(place)

game_end = False
corret_words = []

while not game_end:
    time.sleep(0.75)
    print(f"─────────────────────────{lives}/6 LİVES LEFT────────────────────────────────")
    time.sleep(1)
    user_guess = input("Guess a letter: ").lower()
    print("Being Checked...")
    time.sleep(1.5)
    if user_guess in corret_words:
        print(f"You've already guessed {user_guess}")
    display = ""

    for letter in random_words:
        if letter == user_guess:
            display += letter
            corret_words.append(letter)
        elif letter in corret_words:
            display += letter
        else:
            display += "_"
    print("Word to guess: "+ display)
    print(display)
    if user_guess not in random_words:
        lives -=1
        print(f"You guessed {user_guess},that's not in the word. You lose a life!")
        if lives == 0:
            game_end = True
            print("─────────────────────────YOU LOSE!────────────────────────────────")
            print(f"               İT WAS {random_words}".upper())
            break
    if "_" not in display:
        game_end = True
        print(wordsss.win)
        break
    time.sleep(1.5)
    print(wordsss.hangman[lives])
    
