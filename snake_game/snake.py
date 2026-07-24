from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
# 1. Increased from 1 to 20 so segments step exactly one full square length
MOVE_DISTANCE = 20  
RIGHT = 0
LEFT = 180
UP = 90
DOWN = 270

class Snake:

    def __init__(self):
        self.seg = []
        self.create_snake()
        # 2. DEFINED THE HEAD: Links self.head to the very first segment in your list
        self.head = self.seg[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            new_turtle = Turtle(shape="square")
            new_turtle.color("white")
            new_turtle.penup()
            # 3. Speed 0 eliminates individual animation lag
            new_turtle.speed(0)
            new_turtle.goto(position)
            self.seg.append(new_turtle)

    def move(self):
        for body in range(len(self.seg) - 1, 0, -1):
            new_x = self.seg[body - 1].xcor()
            new_y = self.seg[body - 1].ycor()
            self.seg[body].goto(new_x, new_y)
        # 4. Replaced seg[0] with self.head for consistency
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
