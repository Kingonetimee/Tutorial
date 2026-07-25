from turtle import Turtle
SCORE = 0
ALIGNMENT = "center"
FONT = ('Courier', 80, 'normal')

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = SCORE
        self.r_score = SCORE
        self.update_score()

        
    def update_score(self):
        self.clear()
        self.goto(100, 200)
        self.write(self.r_score, align= ALIGNMENT, font= FONT)
        self.goto(-100, 200)
        self.write(self.l_score, align= ALIGNMENT, font= FONT)


    def right_score(self):
        self.r_score += 1
        self.update_score()

    def left_score(self):
        self.l_score += 1
        self.update_score()
