from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
import random


screen = Screen()
screen.setup(width= 600, height= 600)
screen.bgcolor((0,0,0))
screen.title("Snake Game")
screen.tracer(0)

screen.update()
game_is_on = True
snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_left, "Left")
screen.onkey(snake.move_right, "Right")
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.update_score()
        snake.extend()
        screen.update()
    screen.update()
    for segment in snake.pieces_of_snake[1:]:
      if snake.head.distance(segment) < 10 and len(snake.pieces_of_snake) > 3:
            print(snake.head.distance(segment))
            game_is_on = False
            scoreboard.game_over()

    if snake.head.xcor()  > 280 or snake.head.xcor()  < -280 or snake.head.ycor() > 280 or  snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()
    

screen.exitonclick()
