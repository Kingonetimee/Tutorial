import turtle as t
import random as r

screen = t.Screen()
screen.setup(width=500, height=400)
user_guess = screen.textinput(
    title="Make a Bet", prompt="Which color will win the race? (yellow/green/red/blue/purple)"
).lower()

# 2. Configuration Data
colors = ["yellow", "green", "red", "blue", "purple"]
y_positions = [-100, -50, 0, 50, 100]
all_turtles = []

# 3. Create and position all turtles dynamically using a loop
for index in range(len(colors)):
    new_turtle = t.Turtle(shape="turtle")
    new_turtle.color(colors[index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[index])  # -230 gives them a bit more space from edge
    all_turtles.append(new_turtle)

# 4. Main Game Loop
play = True
while play:
    for turtle in all_turtles:
        # Move each turtle a random distance
        distance = r.randint(1, 20)
        turtle.forward(distance)

        # Check if this turtle crossed the finish line (X-coordinate > 220)
        if turtle.xcor() > 230:
            play = False
            winning_color = turtle.pencolor()

            # Announce results
            if winning_color == user_guess:
                print(f"You won! The {winning_color} turtle finished first!")
            else:
                print(f"You lost! The {winning_color} turtle won the race.")
            
            break  # Exit the turtle loop immediately

screen.exitonclick()