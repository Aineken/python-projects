from turtle import Turtle, Screen
from pandas import read_csv, DataFrame
from names import Names
import time

screen = Screen()
screen.title("U.S. States Game")
screen.bgpic("blank_states_img.gif")
screen.tracer(0)

data = read_csv("50_states.csv")
states = data["state"].to_list()

state_numbers = []


while len(state_numbers) < 50:
    numbers = f"{len(state_numbers)}/{len(states)}"
    answer_state = screen.textinput(title=f"{numbers} Guess the State", prompt="What's another state's name?").title()
    if answer_state in states:
        state_cord = data[data["state"] == answer_state]
        state_cord = state_cord.to_dict(orient="records")[0]
        cords = {"x": state_cord["x"], "y": state_cord["y"]}
        Names(cords, answer_state)
        state_numbers.append(answer_state)
        states.remove(answer_state)
    elif answer_state == "Exit":
        df = DataFrame(states)
        df.to_csv("states_to_learn.csv")

    screen.update()
    time.sleep(0.1)

screen.mainloop()
