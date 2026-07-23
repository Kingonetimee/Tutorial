import random

COM_GUESS = random.randint(1, 101)
# def play():
#     guess = int(input("Make a guess: "))
#     return guess

def easy():
    lives = 10
    game_over = False
    while not game_over:
        if lives > 0:
            print(f"You have {lives} attempts remaining to guess a number.")
            guess = int(input("Make a guess: ")) 
            
            if COM_GUESS != guess:
                if COM_GUESS > guess:
                   print(f"Too Low. \nGuess again.")
                elif COM_GUESS < guess:
                    print(f"Too High. \nGuess again.")   
                lives -= 1         
            elif COM_GUESS == guess:
                print("You are correct")
                game_over = True    
        else:
            if COM_GUESS > guess:
               print(f"Too Low. \nYou've run out of guesses, You Lose!!!  The number is {COM_GUESS}")
               game_over = True       
            elif COM_GUESS < guess:
               print(f"Too High. \nYou've run out of guesses, You Lose!!! The number is {COM_GUESS}")  
               game_over = True     


def hard():
    lives = 5
    game_over = False
    while not game_over:
        if lives == 0:
            if COM_GUESS > guess:
               print(f"Too Low. \nYou've run out of guesses, You Lose!!!  The number is {COM_GUESS}") 
               game_over = True      
            elif COM_GUESS < guess:
               print(f"Too High. \nYou've run out of guesses, You Lose!!! The number is {COM_GUESS}")
               game_over = True          
        elif lives > 0:
            print(f"You have {lives} attempts remaining to guess a number.")
            guess = int(input("Make a guess: ")) 
            
            if COM_GUESS != guess:
                if COM_GUESS > guess:
                   print(f"Too Low. \nGuess again.")
                elif COM_GUESS < guess:
                    print(f"Too High. \nGuess again.")   
                lives -= 1         
            elif COM_GUESS == guess:
                print("You are correct")
                game_over = True    


def play_game():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        return easy()
    elif difficulty == "hard":
        return hard()
    else: 
        print("Wrong Input")
        play_game()



print("Welcome to the Number Guessing Game. \nI am thinking of a Number between 1 and 100")
play_game()