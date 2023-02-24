from turtle import Turtle
class Scoreboard(Turtle):
    score = -1
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0,280)
        self.update_score()

    
    def update_score(self):
        self.clear()
        self.score = self.score + 1
        self.pencolor("white")
        text = "score :  " + str(self.score)
        self.write(arg=text, align="center", move= False, font=("Courier" , 18 , 'normal'))


    def game_over(self):
        self.goto(0,0)
        self.write(arg="GAME OVER", align="center", font=("Courier", 25, 'normal'))