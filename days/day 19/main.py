from turtle import Turtle, Screen


aktos = Turtle()
screen = Screen()
screen.listen()


def move_forward():
    aktos.forward(10)

def move_backward():
    aktos.backward(10)

def turn_left():
    aktos.setheading(aktos.heading()-10)
    # aktos.left(10)
def turn_right():
    # aktos.right(10)
    aktos.setheading(aktos.heading()-10)

def clear():
    aktos.clear()
    aktos.penup()
    aktos.home()
    aktos.pendown()



screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear)








screen.exitonclick()
