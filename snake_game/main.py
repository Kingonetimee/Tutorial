from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# 1. Screen Setup (Run this ONCE outside the function)
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game") 
screen.tracer(0)

# Create instances globally so onkey can access them cleanly
snake = Snake()
food = Food()
score = Scoreboard()

game = True  

while game:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Collision with food
    if snake.head.distance(food) < 15:
        score.increase_score()
        snake.grow()
        food.refresh()

    # Collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset()
        snake.reset()
        
        

    # Collision with tail
    for segment in snake.seg[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()
            

    # 2. Key Bindings (Run this ONCE outside the function)
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")


    

screen.exitonclick()
