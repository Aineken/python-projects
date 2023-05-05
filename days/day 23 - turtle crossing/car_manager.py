from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.move_distance = STARTING_MOVE_DISTANCE
        self.current_number = 1

    def create_car(self):
        if self.current_number == 1:
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.speed("fastest")
            new_car.setheading(180)
            new_car.goto(310, random.randint(-250, 250))
            self.all_cars.append(new_car)
        self.current_number = (self.current_number + 1) % 7

    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.move_distance)

    def level_up(self):
        self.move_distance += MOVE_INCREMENT

    def reset_position(self):
        self.goto(310, random.randint(-280, 280))
        self.color(random.choice(COLORS))
        self.move_distance = STARTING_MOVE_DISTANCE
