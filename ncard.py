from random import choice






def deal_card():
    card = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    deal = choice(card)
    return deal

def calculate(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if  11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
         
    return sum(cards)        

def compare(mine, computer):
    if mine == computer:
        return "It is a Draw!!!"
    elif computer == 0:
        return "lose, Opponent has Blackjack!!!"
    elif mine == 0:
        return "You Win with Blackjack!!!"
    elif computer > 21:
        return "Opponent went over, You Win!!!"
    elif mine > 21 :
        return "You went over, You Lose!!!"
    elif computer < mine:
        return "You win!!!"
    else:
        return "You lose!!!"
   
def play_game():
    my_card = []
    com_card = []
    is_game_over = False
    for _ in range(2):
        my_card.append(deal_card())
        com_card.append(deal_card())

    while not is_game_over:
        mine = calculate(my_card)
        computer = calculate(com_card)
        print(f"Your Cards: {my_card}, Current score: {mine} ")
        print(f"Computer first card: {com_card[0]}")

        if mine == 0 or computer == 0 or mine > 21:
            is_game_over = True
            
        else:
            add_card = input("Type 'y' to get another card, type 'n' to pass: ")
            if add_card == "y":
                my_card.append(deal_card()) 
                mine = calculate(my_card)
            elif add_card == "n":
                is_game_over = True
            else:
               print("Invalid Input")
               add_card
                

    while computer != 0 and computer < 17:
        com_card.append(deal_card())
        computer = calculate(com_card)

    print(f"Your Cards: {my_card}, Your score: {mine} ")
    print(f"Computer Cards: {com_card}, Computer score: {computer} ")
    print(compare(mine, computer))

playing = True
while playing:
    play = input("Do you want to play a game of Blackjack?, Type 'y' or 'n': ")
    if play == "y":
        play_game()
    elif play == "n":
        playing = False
    else:
        print("Invalid Input")
        play
