import turtle as t

tim = t.Turtle()
screen = t.Screen()


def move(x):
  for _ in range(x):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()


move(15)

screen.exitonclick()
