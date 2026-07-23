from random import choice


word_list = ["ardvark", "baboon", "camel"]
chosen_word = choice(word_list)

display = []
lives = 6
for letter in chosen_word:
    display += "_"

print(display)

while "_" in display:
    guess = input("Guess a letter: ").lower()

    for letter in display:
        if guess == letter:
            print(f"You've already guessed {guess}")
            break
    
    for i in range(len(chosen_word)):
        if guess == chosen_word[i]:
            display[i] = guess
         
    print(display)
        

    if guess not in chosen_word:
        print(f"{guess} is not in the word.")
        lives -= 1
        print(f"You have {lives} lives left.")
        if lives == 0:
            print("You lose!")
            break


    if "_" not in display:
        print("You win!")




