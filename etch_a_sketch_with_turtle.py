from turtle import Turtle,Screen

tim = Turtle()

def move():
    tim.forward(10)

def left():
    tim.left(10)

def right():
    tim.right(-10)

def back():
    tim.back(10)

def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen = Screen()
screen.listen()
screen.onkey(move,key="w")
screen.onkey(left,key="a")
screen.onkey(right,key="d")
screen.onkey(back,key="s")
screen.onkey(fun=clear_screen,key="c")
screen.exitonclick()