from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("my snake game")
screen.tracer(0)

snake = []

for number in range(3):
    turtle = Turtle(shape="square")
    turtle.color("white")
    turtle.penup()
    turtle.goto(number * -20, 0)
    snake.append(turtle)

def move_forward():
    for each_snake in snake:
        each_snake.forward(20)
        screen.update()

is_game_on = True
count = 0
while count<30:
    move_forward()
    count += 1


screen.exitonclick()