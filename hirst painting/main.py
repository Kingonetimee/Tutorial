import colorgram as c
import turtle as t
import random as r

t.colormode(255)
color_list = [(199, 175, 117), (125, 36, 24), (187, 158, 51), (170, 104, 56), (5, 57, 83), (222, 223, 226), (200, 216, 204), (108, 67, 85), (39, 36, 35), (86, 142, 59), (20, 122, 176), (110, 161, 175), (75, 39, 47), (9, 67, 47), (64, 153, 137), (133, 41, 43), (184, 98, 80), (179, 201, 186), (209, 200, 115), (179, 174, 177), (151, 176, 165), (93, 142, 156), (28, 80, 59), (194, 190, 192), (17, 78, 99), (212, 184, 174), (142, 117, 123), (175, 198, 204)]

timmy = t.Turtle()
timmy.speed(0)
timmy.penup()
timmy.hideturtle()
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)

def dot():
    for _ in range(10):
        timmy.color(r.choice(color_list))
        timmy.dot(20)
        timmy.forward(50)
    

for _ in range(10):
    dot()
    timmy.setheading(90)
    timmy.forward(50)
    timmy.setheading(180)
    timmy.forward(500)
    timmy.setheading(0)
    
   

screen = t.Screen()
screen.exitonclick()
