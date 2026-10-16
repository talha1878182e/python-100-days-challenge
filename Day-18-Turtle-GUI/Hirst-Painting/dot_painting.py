"""
import colorgram

rgb_colors= []
colors = colorgram.extract("imagea.jpg", 100)
for color in colors:https://github.com/talha1878182e/python-100-days-challenge/tree/main/Day-18-Turtle-GUI
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r,g,b)
    rgb_colors.append(new_color)
print(rgb_colors)
"""


color_list=[(245, 234, 239), (233, 242, 236), (208, 158, 96), (234, 213, 101), (41, 104, 144), (149, 78, 57), (130, 168, 194), (202, 137, 162), (148, 65, 83), (24, 40, 55), (204, 90, 68), (169, 159, 55), (139, 180, 152), (193, 89, 121), (59, 117, 93), (26, 44, 36), (223, 171, 187), (63, 46, 34), (91, 154, 104), (44, 161, 182), (237, 212, 7), (226, 175, 167), (13, 96, 75), (41, 59, 99), (179, 189, 213), (99, 125, 168), (65, 33, 43), (104, 43, 59), (172, 204, 182), (108, 46, 38), (158, 204, 215), (76, 69, 37), (9, 87, 109)]
import turtle
import random
tim = turtle.Turtle()
turtle.colormode(255)
screen = turtle.Screen()
tim.speed("fastest")
tim.pensize(15)

def side():
    for _ in range(10):
        tim.color(random.choice(color_list))
        tim.forward(1)
        tim.penup()
        tim.forward(30)
        tim.pendown()
def square():
    for _ in range(4):
        side()
        tim.left(90)
square()
screen.exitonclick()

