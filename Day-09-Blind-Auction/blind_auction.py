
def find_highest_bidder(bidding_dict):
    winner = ""
    highest_bid = 0

    max(bidding_dict)

    for bidder in bidding_dict:
        bid_amount = bidding_dict[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

binds = {}
continue_bidding = True
while continue_bidding == True:
    name = input("What is your name?: ")
    price = float(input("What is your price?: $ "))
    binds[name] = price
    should_continue = input("Do you want to continue? (y/n): ")
    if should_continue == "n":
        continue_bidding = False
        find_highest_bidder(binds)
    elif should_continue == "y":
        print("\n"*15)

