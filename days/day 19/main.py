from random import randint
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=500)
screen.bgcolor("black")
screen.listen()
color_name = screen.textinput(title="Select the color", prompt="Enter the color you want to select: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
colors.sort(reverse=True)
turtles = []

for color in colors:
    turtle = Turtle("turtle")
    turtle.color(color)
    turtle.penup()
    turtle.goto(x=-230, y=colors.index(color) * 50 - 125)
    turtles.append(turtle)


x = Turtle()


def line():
    x.backward(250)
    x.dot(25, "yellow")
    x.color("white")
    x.forward(500)
    x.backward(250)


line()
x.setheading(90)
line()

is_play = False
if color_name:
    is_play = True

while is_play:
    for turtle in turtles:
        turtle.forward(randint(0, 10))
        if turtle.xcor() > 230:
            is_play = False
            winning_color = turtle.pencolor()
            if winning_color == color_name:
                print(f"You won! The {winning_color} turtle is the winner!")
            else:
                print(f"You lost! The {winning_color} turtle is the winner!")

screen.exitonclick()
