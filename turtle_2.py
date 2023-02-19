from turtle import Turtle,Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.color("Goldenrod")
screen = Screen()
screen.colormode(255)
# tim.forward(100)
# tim.left(90)
# tim.forward(100)
# tim.left(90)
# tim.forward(100)
# tim.left(90)
# tim.forward(100)
# tim.left(90)
# tim.forward(100)
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# for side in range(3,10):
#     for _ in range(side):
#         tim.forward(100)
#         tim.left(360/side)
#     tup = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
#     print(tup)
#     tim.color(tup)
# moves = [tim.left,tim.right,tim.forward,tim.backward]
# tim.pen(pensize=10,speed=0)
# for _ in range(2000):
#     function = random.choice(moves)
#     if function == tim.left or function == tim.right:
#         function(90)
#     else:
#         function(30)
#     tup = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
#     tim.color(tup)

#alternatively

# direction = [0,90,180,270]
# tim.speed(0)
# tim.pensize(15)
# for _ in range(200):
#     tim.forward(20)
#     tim.setheading(random.choice(direction))
#     tup = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
#     tim.pencolor(tup)
#     screen.bgcolor(tup)

# for _ in range(200):
#     tup = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
#     screen.bgcolor(tup)

#spirograph
def draw_spirograph(size_of_gap):
    tim.speed(0)
    for i in range(0,360,size_of_gap):
        tim.circle(100)
        # tim.tilt(30)
        tim.setheading(i)
        tup = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        tim.pencolor(tup)


draw_spirograph(20)

screen.exitonclick()
