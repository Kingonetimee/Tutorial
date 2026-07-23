from data import data
from art import logo
from art import vs
from random import choice

def pick():
    return choice(data)

first_pick = pick()
second_pick = pick()
if first_pick == second_pick:
    second_pick = pick()
score = 0

def question():
    print(f"compare A: {first_pick['name']}, a {first_pick['description']}, from {first_pick['country']}")
    print(vs)
    print(f"Against B: {second_pick['name']}, a {second_pick['description']}, from {second_pick['country']}")

print(logo)
playing = True
while playing:
    question()
    user_pick = input("Who has more follower? Type 'A' or 'B': ").upper()
    if user_pick == "A":
        if first_pick['follower_count'] > second_pick['follower_count']:
            score += 1
            second_pick = pick()
            print(logo)
            print(f"You are correct. Current Score: {score} ")
        elif first_pick['follower_count'] < second_pick['follower_count']:
            print(f"Sorry, that's wrong!  Final Score: {score}")
            playing = False
    elif user_pick == "B":
        if first_pick['follower_count'] < second_pick['follower_count']:
            score += 1
            first_pick = second_pick
            second_pick = pick()
            print(logo)
            print(f"You are correct. Current Score: {score} ")
        elif first_pick['follower_count'] > second_pick['follower_count']:
            print(f"Sorry, that's wrong!  Final Score: {score}")
            playing = False
