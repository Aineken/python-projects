from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position="right"):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.speed("fastest")
        if position == "left":
            self.goto(-350, 0)
        else:
            self.goto(350, 0)

    def up(self):
        if self.ycor() < 240:
            self.goto(self.xcor(), self.ycor() + 20)

    def down(self):
        if self.ycor() > -240:
            self.goto(self.xcor(), self.ycor() - 20)


