from car_manager import CarManager
from turtle import Turtle
import time 

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(STARTING_POSITION)
        self.car_list = []
        self.shape("turtle")
        self.setheading(90)

            
    def move_turtle(self):
        self.forward(10)

    def move_to_begining(self):
        self.goto(STARTING_POSITION)