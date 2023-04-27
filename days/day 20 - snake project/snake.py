from turtle import Turtle
from random import randint

UP = 90
LEFT = 180
RIGHT = 0
DOWN = 270
STEP_MOVE = 20





class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for number in range(5):
            turtle = Turtle("circle")
            turtle.color((randint(0,255),randint(0,255),randint(0,255)))
            turtle.penup()
            turtle.goto(number * -STEP_MOVE, 0)
            self.snake.append(turtle)

    def move(self):
        for snake_number in range(len(self.snake) - 1, 0, -1):
            self.snake[snake_number].setposition(self.snake[snake_number - 1].position())
        self.head.forward(STEP_MOVE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
