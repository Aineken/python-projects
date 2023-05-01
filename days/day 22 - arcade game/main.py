from turtle import Screen
from paddle import Paddle



screen = Screen()
paddle = Paddle()

screen.setup(800, 600)
screen.colormode(255)
screen.bgcolor("black")
screen.title("My Arcade Game")


screen.listen()
screen.onkey(paddle.up, "Up")
screen.onkey(paddle.down, "Down")




screen.exitonclick()