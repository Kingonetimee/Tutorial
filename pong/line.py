from turtle import Turtle

class Line(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.pensize(5)
        self.speed(0)
        self.penup()
        self.goto(0, 300)
        self.setheading(270)
        self.create_line()

    def create_line(self):
        while self.ycor() > -300:
            self.penup()
            self.forward(15)
            self.pendown()
            self.forward(15)