from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.tracer(0)

screen.setup(800, 600)
screen.colormode(255)
screen.bgcolor("black")
screen.title("My Arcade Game")

r_paddle = Paddle()
l_paddle = Paddle("left")
ball = Ball()
score = Scoreboard()

screen.listen()

screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

is_game_on = True
while is_game_on:

    screen.update()
    time.sleep(0.1)
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    elif ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    elif ball.xcor() > 380:
        score.update_score("left")
        ball.reset_position()
        screen.update()
        time.sleep(1)
    elif ball.xcor() < -380:
        score.update_score("right")
        ball.reset_position()
        screen.update()
        time.sleep(1)

screen.exitonclick()
