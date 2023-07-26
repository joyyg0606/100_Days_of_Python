import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor('black')
screen.setup(width=600, height=600)
screen.tracer(0)

car_manager = CarManager()
scoreboard = Scoreboard()
player = Player()

screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(car_manager.car_speed)
    screen.update()
    
    car_manager.create_car()
    car_manager.move_car()

    if player.ycor() == 290:
        player.reset_position()
        car_manager.speed_up_cars()
        scoreboard.new_level()

    for car in car_manager.all_cars:
        if car.distance(player) < 19:
            scoreboard.final_scores()
            game_is_on = False

screen.exitonclick()