from turtle import Turtle

SCORE = 0
ALIGNMENT = "center"
FONT = ('Courier', 24, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = SCORE
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 270)
        self.update()

    def update(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font= FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game over!!!", align=ALIGNMENT, font=FONT)
          
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update()
       
    