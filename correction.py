from random import choice

word_list = ["apple","ball","cat","replenish","illiterate"]
lives = 6
dash = []

word = choice(word_list)
for i in word:
    dash += "_"
print (dash)

while "_" in dash:

    guess_word = input("Guess a letter: ").lower()

    for i in dash:
        if guess_word == i:
            print(f"You've already guessed {guess_word}")
            break

    for i in range(len(word)):
        if guess_word == word[i]:
            dash[i] = guess_word
    print(dash)

    if guess_word not in word:
        print(f"Sorry, {guess_word} is not in the word")
        lives -= 1
        print(f"You have {lives} live left")
        if lives == 0:
            print("Ohh!! YOU LOSE")
            break

    if not "_" in dash:
        print("Congratulations, You Win!!!")
