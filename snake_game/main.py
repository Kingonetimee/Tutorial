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



def snake_game():
    global snake, score
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
            game = False

        # Collision with tail
        for segment in snake.seg[1:]:
            if snake.head.distance(segment) < 10:
                game = False

        # 2. Key Bindings (Run this ONCE outside the function)
        screen.listen()
        screen.onkey(snake.up, "Up")
        screen.onkey(snake.down, "Down")
        screen.onkey(snake.left, "Left")
        screen.onkey(snake.right, "Right")

    # Game over logic happens AFTER the while loop finishes cleanly
    score.game_over()
    
    # Prompt user for restart safely
    restart = screen.textinput(title="Game Over!!!", prompt="Do you want to restart? 'Y OR N'")
    
    if restart and restart.lower() == "y":
        # Clear old snake body from screen before making a new one
        for segment in snake.seg:
            segment.goto(1000, 1000) # Send old body off-screen
        
        # Reset global objects completely
        
        snake = Snake()
        score.clear() # Clear old scoreboard text
        score = Scoreboard()
        
        # Restart the game loop cleanly without nesting functions
        snake_game()

# Run the game for the first time
snake_game()
screen.exitonclick()
