import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("blue")
        self.penup()
        self.shape("circle")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        x_pos = random.randrange(-280, 280, 10)
        y_pos = random.randrange(-280, 280, 10)
        self.goto(x_pos, y_pos)
