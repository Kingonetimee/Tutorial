from random import choice 

def blackjack():
    num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    my_num = []
    com_num = []
    Should_continue = True
    def winner():
        if sum(my_num) > sum(com_num) and sum(my_num) < 21:
            print("You win!!!")
        else:
            print("Dealer Wins!!!")

    while Should_continue: 
        if input("Do you want to play a game of Blackjack?, Type 'y' or 'n': ") == "y":
            my_num = [choice(num), choice(num)]
            com_num = [choice(num)]

            print(my_num)
            print(com_num)

            if input("Type 'y' to get another card, type 'n' to pass: ") == "y":
                my_num.append(choice(num))
                com_num.append(choice(num))
                sum_com = sum(com_num)
                if sum_com < 17:
                    com_num.append(choice(num))
                    new_sum_com = sum(com_num)
                    print(f"Dealer Cards are {com_num} and the Total is {new_sum_comsum_com}")
            
                print(f"Your Cards are {my_num} and the Total is {sum(my_num)}")
                print(f"Dealer Cards are {com_num} and the Total is {sum_com}")
                winner()
            else:
                com_num.append(choice(num))
                if sum_com < 17:
                    com_num.append(choice(num))
                    sum_com = sum(com_num)
                print(f"Your Cards are {my_num} and the Total is {sum(my_num)}")
                print(f"Dealer Cards are {com_num} and the Total is {sum_com}")
                winner()
        else:
            Should_continue = False
            blackjack()

blackjack()