from turtle import Turtle,Screen
import random


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title= "Make your bet", prompt= "Which will win the race? Enter a color : ")
color = ["red", "orange", "yellow", "green", "violet", "blue"]
turtles = []
for t in color:
    a_turtle = Turtle(shape="turtle")
    a_turtle.color(t)
    turtles.append(a_turtle)

nth_racer = 0
for i in range(-180,180,60):
    turtles[nth_racer].penup()
    turtles[nth_racer].goto(x= -240 , y = i)
    nth_racer += 1

race_end = False
while race_end == False:
    for t in turtles:
        position = t.position()
        if position[0] == 240:
            winner = t.color()[0]
            race_end = True
    random.choice(turtles).forward(random.randint(0,10))

if user_bet == winner:
    print(f"You have won the bet!! {winner} won!")
else:
    print(f"You have lost the bet! {winner} won")
screen.exitonclick()