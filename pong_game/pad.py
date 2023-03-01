from turtle import Turtle

class Pad(Turtle):
    
    def __init__(self,xpos):
        super().__init__()
        self.xpos = xpos
        self.create_pad(self.xpos)
     
        
    def create_pad(self,xposition):
        
        
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid= 5, stretch_len= 1)
        self.goto(x=xposition, y=0)
        return 
        

    def pad_up(self):
        new_position = self.ycor() + 20
        self.goto(x= self.xpos, y=new_position)

    def pad_down(self):
        new_position = self.ycor() - 20
        self.goto(x= self.xpos, y=new_position)