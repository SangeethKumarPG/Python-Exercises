from turtle import Turtle, Screen
import time
import random
screen = Screen()
screen.setup(width= 600, height= 600)
screen.bgcolor((0,0,0))
screen.title("Snake Game")
screen.tracer(0)
pieces_of_snake = []
for i in range(-40,1,20):
    snake = Turtle()
    snake.penup()
    snake.shape("square")
    snake.color("white")
    snake.goto(x=i, y=0)
    pieces_of_snake.append(snake)
    print(snake.position())
screen.update()
print("===========")

count_of_bubble = 0
def left():
    pieces_of_snake[len(pieces_of_snake)-1].left(90)
    # pieces_of_snake[len(pieces_of_snake)-1].forward(20)
    forward()
    screen.update()


def right():
    pieces_of_snake[len(pieces_of_snake)-1].right(90)
    forward()
    # pieces_of_snake[len(pieces_of_snake)-1].forward(20)
    screen.update()

def add_tail():
    new_snake = Turtle()
    new_snake.shape("square")
    new_snake.color("white")
    pieces_of_snake.append(new_snake)

def forward():
    # print("Forward")
    for i in range(0,len(pieces_of_snake)):
        print(len(pieces_of_snake))
        if i+1 <= len(pieces_of_snake) -1:
            position = pieces_of_snake[i+1].position()
            pieces_of_snake[i].goto(position)
        else:
            pieces_of_snake[i].forward(20)
    screen.update()


def is_out_of_bounds():
    head_position = pieces_of_snake[len(pieces_of_snake)-1].position()
    if head_position[0] < -290 or head_position[1] < -290:
        return True
    elif head_position[0] > 290 or head_position[1] > 290:
        return True
    else:
        return False

def goal_not_achieved(bubble):
    head_position = pieces_of_snake[len(pieces_of_snake)-1].position()
    if head_position == bubble.position():
        bubble.clear()
        return True
    else:
        return False

def generate_a_bubble():
    bubble = (random.randint(-280,280),random.randint(-280,280))
    objective = Turtle()
    objective.shape("circle")
    objective.color("red")
    objective.penup()
    objective.goto(bubble)
    return objective
# screen.onkey(fun=forward, key="Up")
screen.listen()
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    forward()
    if count_of_bubble == 0:
        bubble = generate_a_bubble()
   
    while goal_not_achieved(bubble) == False and is_out_of_bounds() == False:
        screen.onkey(fun=left, key="Left")
        screen.onkey(fun= right, key="Right")
        time.sleep(0.1)
        forward()
    screen.onkey(fun=left, key="Left")
    screen.onkey(fun= right, key="Right")
    # for pos in pieces_of_snake:
    #     print(pos.position())
    
    if is_out_of_bounds == True:
        game_is_on = False
    screen.update()
    # break
    

screen.exitonclick()
