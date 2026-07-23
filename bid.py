bid = {}
bidding_finished = False

def highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")    
        


while not bidding_finished:
    name = input("what is youur name: ")
    price = int(input("what is your bid price: $")) 
    bid[name] = price
    should_continue = input("Are there other users? Type 'yes' or 'no': ")
    if should_continue == "no":
        bidding_finished = True
        highest_bidder(bid)   
  

