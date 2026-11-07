bids = {}
should_continue = True
logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while should_continue == True:
    print(logo)
    name = input("What is your name? \n")
    price = int(input("What is your bid? \n$"))
    bids[name] = price
    continue_bidding = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if continue_bidding == "no":
        should_continue = False
        find_highest_bidder(bids)
    elif continue_bidding == "yes":
        print("\n" * 90)
