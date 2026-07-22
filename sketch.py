import turtle as t


tim = t.Turtle()
screen = t.Screen()

def clear():
    tim.penup()
    tim.clear()
    tim.home()
    tim.pendown()
def move_c():
    tim.right(20)
def move_cc():
    tim.left(20)
def move_back():
    tim.backward(20)
def move_forward():
    tim.forward(20)


screen.onkey(move_forward, "w")
screen.onkey(move_back, "s")
screen.onkey(move_cc, "a")
screen.onkey(move_c, "d")
screen.onkey(clear, "c")
screen.listen()
screen.exitonclick()