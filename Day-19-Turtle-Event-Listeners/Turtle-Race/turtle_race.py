from turtle import *
import random

screen = Screen()
screen.setup(width=500, height=400)

wallet = 100
colors = ["red", "blue", "green", "yellow", "orange", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]

pen = Turtle()
pen.hideturtle()
pen.penup()
screen.bgpic("backroun.png")
play_again = True

while play_again and wallet > 0:
    pen.clear()

    user_bet = screen.textinput(title="Make your bet",
                                prompt=f"Balance: ${wallet}\nWhich turtle will win? Enter a color (red, blue...): ")

    if not user_bet:
        break

    bet_amount_str = screen.textinput(title="Bet Amount",
                                      prompt=f"Your balance: ${wallet}\nHow much do you want to bet?")

    try:
        bet_amount = int(bet_amount_str)
    except:
        bet_amount = 10

    if bet_amount > wallet or bet_amount <= 0:
        pen.goto(0, 0)
        pen.write("Invalid bet amount!", align="center", font=("Arial", 16, "bold"))
        break

    wallet -= bet_amount
    all_turtles = []

    for turtle_index in range(0, 6):
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(colors[turtle_index])
        new_turtle.penup()
        new_turtle.goto(x=-230, y=y_positions[turtle_index])
        all_turtles.append(new_turtle)

    is_race_on = True

    while is_race_on:
        for turtle in all_turtles:
            random_distance = random.randint(0, 10)
            turtle.forward(random_distance)

            if turtle.xcor() > 230:
                is_race_on = False
                winning_color = turtle.pencolor()
                multiplier = 2

                pen.goto(0, 120)

                if winning_color == user_bet.lower():
                    winnings = bet_amount * multiplier
                    wallet += winnings
                    pen.color("green")
                    pen.write(f"YOU WON! The {winning_color.capitalize()} turtle won.\nBalance: ${wallet}",
                              align="center", font=("Arial", 16, "bold"))
                else:
                    pen.color("red")
                    pen.write(f"YOU LOST! The {winning_color.capitalize()} turtle won.\nBalance: ${wallet}",
                              align="center", font=("Arial", 16, "bold"))

                break

    for turtle in all_turtles:
        turtle.hideturtle()

    if wallet > 0:
        response = screen.textinput(title="Play Again?", prompt="Do you want to play again? (yes/no): ")
        if response and response.lower() == "yes":
            play_again = True
        else:
            play_again = False
    else:
        pen.goto(0, 80)
        pen.color("black")
        pen.write("GAME OVER! You ran out of money.", align="center", font=("Arial", 14, "bold"))
        play_again = False

screen.exitonclick()
