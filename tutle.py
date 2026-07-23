import turtle as t
import random as r

t.colormode(255)
t.mode("standard")
timmy = t.Turtle()

def colour():
    red = r.randint(0, 225)
    blue = r.randint(0, 225)
    green = r.randint(0, 225)

    return (red, green, blue)

timmy.speed(0)

def draw(size):
    for i in range (int(360/size)):
        timmy.color(colour())
        timmy.setheading(timmy.heading() + size)
        timmy.circle(100)
    
draw(1)      
# for _ in range(5):
#    timmy.forward(100)
#    timmy.left(72)





my_screen = t.Screen()
my_screen.exitonclick()


