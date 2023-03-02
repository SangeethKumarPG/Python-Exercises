from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):

        self.car_list = []
        self.generate_car()
        self.stop = False
        self.distance = STARTING_MOVE_DISTANCE


    def generate_car(self):
        if random.randint(1,6) == 3 and self.stop == False:
            car = Turtle()
            car.shape("square")
            car.penup()
            car.shapesize(stretch_len=4, stretch_wid=2)
            random_y_position = 0
            x_position = 280
            random_color = random.choice(COLORS)
            car.color(str(random_color))
            random_y_position = random.randint(-250, 250)
            car.goto(x_position, random_y_position)
            self.car_list.append(car)
        

    def move_car(self):
        for car in self.car_list:
            if self.stop == False:
                car.backward(self.distance)


    def increase_car_speed(self):
        self.distance += MOVE_INCREMENT
    
