from turtle import Turtle, Screen
import time
from snake import Snake

snake = Snake()

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game ") 
screen.tracer(0)
screen.listen()




game = True    
while game:
    screen.update()
    time.sleep(0.1)
    snake.move()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")










screen.exitonclick()