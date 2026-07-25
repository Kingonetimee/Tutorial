from turtle import Turtle


UP = 90
DOWN = 270
DISTANCE = 20

class Paddle(Turtle):
    
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.create_paddle(x_cor, y_cor)
        

    def create_paddle(self, x_cor, y_cor):
        """it returns the paddles with given cordinates"""
        self.shape("square")
        self.shapesize(5, 1)
        self.speed(0) 
        self.color("white")
        self.penup()
        self.goto(x_cor, y_cor)

    def up(self):
        """It makes paddle go up by changing its Y cor"""
        new_y = self.ycor() + DISTANCE
        self.sety(new_y)
        

    def down(self):
        """It makes paddle go down by changing its Y cor"""
        new_y = self.ycor() - DISTANCE
        self.sety(new_y)
        