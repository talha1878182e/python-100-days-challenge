import random
import turtle as t

tim = t.Turtle()
screen = t.Screen()

t.colormode(255)


def ramdom_color():
  r = random.randint(0, 255)
  g = random.randint(0, 255)
  b = random.randint(0, 255)
  return (r, g, b)



for side in range(3, 11):
  tim.color(ramdom_color())
  for _ in range(side):
    tim.forward(100)
    tim.right(360 / side)

screen.exitonclick()
