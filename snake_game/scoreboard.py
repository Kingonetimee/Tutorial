from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 24, 'normal')
with open("snake_data.txt") as data:
    h_score = int(data.read())

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = h_score
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 270)
        self.update()
        

    def update(self):
        self.clear()
        self.write(f"Score: {self.score}; High Score: {self.high_score}", align=ALIGNMENT, font= FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("snake_data.txt", mode="w") as data:
                data.write(str(self.high_score))
        self.score = 0
        self.update()

         
    def increase_score(self):
        self.score += 1
        self.update()
       
    