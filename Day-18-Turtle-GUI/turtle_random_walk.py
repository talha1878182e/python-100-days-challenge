import random
import turtle as t
from random import randint

tim = t.Turtle()
screen = t.Screen()
t.colormode(255)



def ramdom_color():
  r = random.randint(0, 255)
  g = random.randint(0, 255)
  b = random.randint(0, 255)
  return r, g, b


tim.pensize(15)
tim.speed("fastest")

for _ in range(200):
    tim.color(ramdom_color())
    tim.forward(randint(20, 50))
    tim.setheading(random.randint(0, 360))

screen.exitonclick()
