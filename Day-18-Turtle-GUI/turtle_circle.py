import random
import turtle as t

repeat_count = int(
    input("How many times to draw? (e.g., 36): ")
)
angle = int(
    input("What should the turning angle be? (e.g., 10, 15, 30): ")
)

screen = t.Screen()
t.colormode(255)

tim = t.Turtle()
tim.speed("fastest")


def random_color():
  r = random.randint(0, 255)
  g = random.randint(0, 255)
  b = random.randint(0, 255)
  return (r, g, b)


for i in range(repeat_count):
  tim.color(random_color())
  tim.circle(100)
  tim.left(angle)
  tim.circle(100)
  tim.left(angle)

screen.exitonclick()
