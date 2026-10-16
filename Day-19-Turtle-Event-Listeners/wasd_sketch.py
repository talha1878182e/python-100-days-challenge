from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def move_back():
    tim.backward(10)


def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)


def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


def up():
    tim.keyup() if hasattr(tim, "keyup") else tim.penup()


def down():
    tim.keydown() if hasattr(tim, "keydown") else tim.pendown()


def show_position():
    print(f"Mevcut Konum: {tim.pos()}, Yön: {tim.heading()}°")


screen.listen()

screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_back)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear)
screen.onkey(key="u", fun=up)
screen.onkey(key="p", fun=down)

screen.onkey(key="space", fun=show_position)

screen.exitonclick()
