from turtle import Turtle

FONT = ("Courier", 12, "normal")
ALIGNMENT = "left"


class Names(Turtle):
    def __init__(self,cords, state):
        super().__init__()
        self.write_text(cords, state)
    def write_text(self, cords, state):
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(int(cords["x"]), int(cords["y"]))
        self.write(state, align=ALIGNMENT, font=FONT)
