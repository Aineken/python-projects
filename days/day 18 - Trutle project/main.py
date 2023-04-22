from turtle import *
from random import randint, choice
from colors import colors



screensize(450, 450)

colormode(255)
speed(0)
penup()
n=-225

hideturtle()    #hides the turtle

def spot_paint(n,range_number=10):
    for _ in range(range_number):
        goto(-225, n)
        for i in range(range_number):
            dot(20, choice(colors))
            if i == range_number-1:
                break
            forward(50)

        n += 50

spot_paint(n)






exitonclick()

# def draw_spirograph(size_of_gap):
#     for _ in range(int(360 / size_of_gap)):
#         width(2)
#         color(random_color(), random_color())
#         circle(r)
#
#         setheading(heading() + size_of_gap)
#
# draw_spirograph(5)

# def random_step():
#     setheading(choice(directions))
#     forward(30)
#
#
# def random_step2():
#     if randint(1, 2) % 2 == 0:
#         left(90)
#     else:
#         right(90)
#     forward(30)

# def draw_shape(lines):
#     for _ in range(lines):
#         left(360 / lines)
#         forward(100)
#
#
# for number in range(3, 11):
#     color(randint(0, 255), randint(0, 255), randint(0, 255))
#     draw_shape(number)

#colors extraction from image using colorgram
# colors = extract('img.png', 20)
# for i in colors:
#     r = i.rgb.r
#     g = i.rgb.g
#     b = i.rgb.b
#     color_all = (r, g, b)
#     if r>240 and g>240 and b>240:
#         pass
#     else:
#         rgb_colors.append(color_all)