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
        self.tail = self.seg[1 : len(self.seg)]

    def create_snake(self):
        for position in STARTING_POSITION:
            bodies = self.bodies() 
            bodies.goto(position)
            self.seg.append(bodies)  

    def reset(self):
        for seg in self.seg:
            seg.goto(1000, 1000)
        self.seg.clear()
        self.create_snake()
        self.head = self.seg[0]
        self.tail = self.seg[1 : len(self.seg)]
        
           
    def bodies(self):
        new_turtle = Turtle(shape="square")
        new_turtle.color("white")
        new_turtle.penup()
        # 3. Speed 0 eliminates individual animation lag
        new_turtle.speed(0)   
        return new_turtle   
            
    def grow(self):    
        # 1. Create a brand new segment
        new_segment = self.bodies()
        
        # 2. Find the position of the current last segment (-1 gets the last item)
        tail_position = self.seg[-1].position()
        
        # 3. Send the new segment to that exact position so it links up smoothly
        new_segment.goto(tail_position)
        
        # 4. Append it to your tracking list
        self.seg.append(new_segment)   

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
 