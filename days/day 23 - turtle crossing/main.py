import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

main_player = Player()
cars = CarManager()
score = Scoreboard()

screen.onkey(main_player.up, "w")


game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move_cars()

    # Detect collision with car.
    for car in cars.all_cars:
        if main_player.distance(car) < 20:
            game_is_on = False
            score.game_over()

    if main_player.ycor() > 270:
        main_player.reset_position()
        time.sleep(1)
        cars.level_up()
        score.update_score()

screen.exitonclick()
