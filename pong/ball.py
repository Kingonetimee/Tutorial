from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.move_speed = 0.1
        self.penup()
        self.y_move = 10
        self.x_move = 10


    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)


    def bounce(self) -> None:
        self.y_move *= -1


    def play_back(self):
        self.move_speed *= 0.9
        self.x_move *= -1

    def reset_position(self):
        self.move_speed = 0.1
        self.goto(0,0)
        self.play_back()
