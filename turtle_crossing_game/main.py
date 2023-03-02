import time
from turtle import Screen
from player import Player
import random
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
game_is_on = True
player = Player()
car_manager = CarManager()
score = Scoreboard()
screen.onkey(fun = player.move_turtle, key="Up")

while game_is_on:
    
    screen.update()
    time.sleep(0.1)

    car_manager.generate_car()
    for car in car_manager.car_list:
        if car.distance(player) < 20:            
            score.game_over()
            car_manager.stop = True
            game_is_on = False
    if player.ycor() > 250:
        score.level_up()
        player.move_to_begining()
        car_manager.increase_car_speed()
    
    car_manager.move_car()
    
screen.exitonclick()