from turtle import Turtle,Screen
from pad import Pad
from ball import Ball
from scoreboard import Scoreboard
import time
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height= 600)
screen.title("pong")
screen.tracer(0)
screen.listen()

lpad = Pad(-350)
rpad = Pad(350)
pong_ball = Ball()
score = Scoreboard()
screen.update()

screen.onkey(fun=lpad.pad_up, key="w")
screen.onkey(fun= lpad.pad_down, key = "s")
screen.onkey(fun=rpad.pad_up, key="Up")
screen.onkey(fun=rpad.pad_down, key="Down")

is_game_over = False

while is_game_over == False:
    pong_ball.move_ball()
    if pong_ball.ycor() > 280 or pong_ball.ycor() < -280:
        pong_ball.bounce_from_wall()
        print(pong_ball.position())
    if pong_ball.distance(rpad) < 50 and pong_ball.xcor() > 320 or pong_ball.distance(lpad) < 50 and pong_ball.xcor() < -320:
        pong_ball.bounce_from_pad()
        # pong_ball.increase_speed()
        

    if pong_ball.xcor() > 380: 
        pong_ball.reset_ball_position()
        score.l_point()

    if pong_ball.xcor() < -380:
        pong_ball.reset_ball_position()
        score.r_point()

    time.sleep(pong_ball.move_speed)
    screen.update()
    

    
screen.exitonclick()