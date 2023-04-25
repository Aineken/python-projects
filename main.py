import turtle
import math

# Set up the turtle
t = turtle.Turtle()
t.speed(0)
t.penup()
t.goto(0, -200)
t.pendown()

# Draw the circle
r = 200
circumference = 2 * math.pi * r
n = 100
angle = 360 / n
for i in range(n):
    t.forward(circumference / n)
    t.left(angle)

turtle.done()
