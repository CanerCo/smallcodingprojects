from replit import clear

logo = '''
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



#HINT: You can call clear() to clear the output in the console.
print(logo)
All_bidders = []

def adding_bids(bidder_name, bid_amount):
    bid_dictionary = {}
    bid_dictionary["name"] = bidder_name
    bid_dictionary["bid"] = bid_amount
    All_bidders.append(bid_dictionary)

is_bidder = True
while is_bidder:
      name = input("What is your name?: ")
      bid = int(input("What's your bid?: $"))
      ask_bidder = input("Are there any other bidders? Type 'yes' or 'no'").lower()
      adding_bids(name, bid)
      if ask_bidder == "yes":
            is_bidder = True
            clear()
      else:
            is_bidder = False



winner_bid = 0
for i in range(0, len(All_bidders)): 
    current_bid =  All_bidders[i]["bid"]
    while current_bid > winner_bid:
        winner_dict = i
        winner_name = All_bidders[i]["name"]
        winner_bid = All_bidders[i]["bid"]
    else:
        winner_name = All_bidders[winner_dict]["name"]
        winner_bid = All_bidders[winner_dict]["bid"]


print(f"The winner is {winner_name} with a bid of ${winner_bid}")


