from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    
    def __init__(self):
        self.pieces_of_snake = []
        self.create_snake()
        self.head = self.pieces_of_snake[0]
    

    def create_snake(self):
        for i in range(-40,1,20):
            self.create_segment((i,0))


    def extend(self):
        self.create_segment(self.pieces_of_snake[-1].position())

    def create_segment(self,position):
        snake = Turtle()
        snake.penup()
        snake.shape("square")
        snake.color("white")
        snake.goto(position)
        self.pieces_of_snake.append(snake)

    def move(self):
        for i in range(len(self.pieces_of_snake)-1,0,-1):
            position = self.pieces_of_snake[i-1].position()
            self.pieces_of_snake[i].goto(position)
        self.head.forward(MOVE_DISTANCE)
    

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)
        # self.move()


    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)
        # self.move()


    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)
        # self.move()


    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)
        # self.move()