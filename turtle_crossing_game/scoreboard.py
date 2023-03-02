from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-200,260)
        self.player_level = 1
        self.pencolor("black")
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg= f"Level : {self.player_level}",font = FONT, align="center")

    def game_over(self):
        self.goto(0,0)
        self.write(arg = "GAME OVER",align = "center", font = FONT)

    def level_up(self):
        self.player_level += 1
        self.update_score()