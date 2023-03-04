from turtle import Turtle
class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.highscore = int(file.read())
        self.penup()
        self.hideturtle()
        self.goto(0,280)
        self.update_score()

    
    def update_score(self):
        self.clear()
        self.pencolor("white")
        text = "score :  " + str(self.score) + " high score : " + str(self.highscore)
        self.write(arg=text, align="center", move= False, font=("Courier" , 18 , 'normal'))


    def game_over(self):
        self.goto(0,0)
        self.write(arg="GAME OVER", align="center", font=("Courier", 25, 'normal'))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.score))
        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()