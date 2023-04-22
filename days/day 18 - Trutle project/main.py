from turtle import *
from random import randint

colormode(255)
speed(4)


def draw_shape(lines):
    for _ in range(lines):
        left(360 / lines)
        forward(100)





for number in range(3,11):
    color(randint(0, 255), randint(0, 255), randint(0, 255))
    draw_shape(number)


exitonclick()