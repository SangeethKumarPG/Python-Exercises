from turtle import Turtle
import random
from pad import Pad

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.width = 20
        self.height = 20
        self.penup()
        self.move_x = 10
        self.move_y = 10
        # self.speed(1)
        self.move_speed = 0.1

    def move_ball(self):
        new_xcor = self.xcor() + self.move_x
        new_ycor = self.ycor() + self.move_y
        self.goto(new_xcor,new_ycor)
 
    def bounce_from_wall(self):
        self.move_y *= -1

    def collition_with_pad(self, lpad, rpad):
        print(lpad , rpad)
        self.move_speed *= 0.9

    def bounce_from_pad(self):
        self.move_x *= -1

    def reset_ball_position(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.bounce_from_pad()

    # def increase_speed(self):
    #     current_speed = self.speed()
    #     if current_speed < 10 and current_speed != 0:
    #         self.speed(current_speed + 1)
    #     else:
    #         self.speed(0)