from turtle import Turtle, Screen

from prettytable import PrettyTable

x = PrettyTable()

x.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
x.add_column("Type", ["Electric", "Water", "Fire"])

x.align["Pokemon Name"] = "l"
x.align["Area"] = "r"
x.align["Pikachu"] = "r"

print(x)

# ayan = Turtle()
#
# ayan.shape("turtle")
#
# ayan.color("red", "yellow")
#
# ayan.backward(200)
#
# canvas = Screen()
# # canvas.setup(width=500, height=400)
# canvas.exitonclick()
