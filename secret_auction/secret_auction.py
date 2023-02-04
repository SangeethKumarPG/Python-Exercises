from art import logo
import os
print(logo)
auction = {}
def new_participant(name,bid_amount):
    participant = {}
    participant["name"] = name
    participant["bid_amount"] = bid_amount
    auction[name] = participant

def check_winner():
    highest_bidder = ""
    highest_bid = 0
    for keys in auction:
        if auction[keys]["bid_amount"] > highest_bid:
            highest_bid = auction[keys]["bid_amount"]
            highest_bidder = auction[keys]["name"]
    
    print(f'{highest_bidder.capitalize()} won the auction for {highest_bid}')



is_closed = False
while is_closed == False:
    name = input("Name of the participant : ")
    bid_amount=int(input("Bidding amount : $"))
    new_participant(name,bid_amount)
    more_participants = input("Type yes to continue the auction \n type no to end bidding : ")
    if more_participants == "no":
        is_closed = True
    elif more_participants == "yes":
        os.system('clear')
    else:
        print(f'invalid option {more_participants}')
check_winner()
