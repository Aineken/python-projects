from turtle import Screen
import time
from snake import Snake

screen = Screen()
screen.listen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("my snake game")
screen.tracer(0)

snake = Snake()
screen.onkey(snake.left, "a")
screen.onkey(snake.down, "s")
screen.onkey(snake.right, "d")
screen.onkey(snake.up, "w")

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()




screen.exitonclick()
