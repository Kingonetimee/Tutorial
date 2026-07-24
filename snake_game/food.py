from turtle import Turtle
import random as r

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5) 
        self.color("blue")
        self.speed(0)
        self.refresh()
        

    def refresh(self):
        r_x = r.randint(-250, 250)
        r_y = r.randint(-250, 250)
        self.goto(r_x, r_y)
