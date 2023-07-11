import os

from blind_auction_art import hammer
print(hammer)

print("Welcome to the secret actuion program.\n")

bidder_list = {}
def add_bidder(bidder_name, bid_amount):
        bidder_list[name] = bid_amount

def find_highest_bidder(winning_bid):
    winning_bid_number = 0
    for bidder in winning_bid:
        bid_amount = int(winning_bid[bidder])
        if bid_amount > winning_bid_number:
            winning_bid_number = bid_amount
            winner = bidder
    os.system('cls||clear')
    print(f"The winner is {winner} with a bid of ${winning_bid_number}")

more_bidders = True
while more_bidders == True:
        
    name = input("What is your name?: ")
    bid_amount = input("What's your bid?: $")

    other_bidders = input("\nAre there any other bidders? Type 'yes' or 'no'\n").lower()
    
    if other_bidders == 'yes':
        os.system('cls||clear')
        add_bidder(bidder_name=name, bid_amount=bid_amount)

    elif other_bidders == 'no':
        more_bidders = False
        add_bidder(bidder_name=name, bid_amount=bid_amount)
        find_highest_bidder(bidder_list)

add_bidder(bidder_name=name, bid_amount=bid_amount)