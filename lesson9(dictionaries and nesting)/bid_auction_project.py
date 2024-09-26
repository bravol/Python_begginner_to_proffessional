# todo-1: Ask the user for the inputs
# a function to find the highest bidder
def find_highest_bidder(bidding_dictionary):
    highest_bid = 0
    winner = ''
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder] #value
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"Winner is {winner} with a bid of $:{highest_bid}")

# todo-2 save data into the dictionary {name: price}
# todo-3: whether if new bids need to be added
bids = {}
continue_bidding = True
while continue_bidding:
    name = input("What is your name?\n ")
    price = int(input("What is your bid? $:"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no':\n ").lower()
    if should_continue == 'no':
        continue_bidding = False
        # a function to find the highest bidder
        find_highest_bidder(bids)
    elif should_continue == "yes":
        print("\n"*20)


# todo-4: compare bids in dictionary

