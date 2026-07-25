import turtle as t
from paddle import Paddle
from ball import Ball
from score import Score
import time


screen = t.Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("PONG GAME")
screen.listen()
screen.tracer(0)

l_paddle = Paddle(-380, 0)
r_paddle = Paddle(370, 0)
ball = Ball()
score = Score()

screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

game = True
while game:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        
        ball.play_back()

   
    if ball.xcor() > 400: 
        score.left_score()
        ball.reset_position()
        
    if ball.xcor() < -400:
        score.right_score()
        ball.reset_position()
        
    


    
    


screen.exitonclick()