from turtle import Turtle, Screen

import heroes

print(heroes.gen())

ayan = Turtle()
# print(dir(method for method in dir(ayan) if not method.startswith('_')))
ayan.shape("turtle")

ayan.color("red", "yellow")
ayan.shapesize(5, 5, 3)

ayan.backward(200)

# ayan.forward(200)
# ayan.left(90)
# ayan.forward(200)
# ayan.right(90)
# ayan.forward(200)
# ayan.right(90)
#
# ayan.forward(200)
# ayan.right(90)
# ayan.forward(200)
# ayan.left(90)
# ayan.forward(200)
# ayan.left(90)
# ayan.forward(200)
# ayan.right(90)
# ayan.forward(200)
# ayan.right(90)

canvas = Screen()
# canvas.setup(width=500, height=400)
canvas.exitonclick()
