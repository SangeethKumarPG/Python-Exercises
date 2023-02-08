from art import logo
import random
print(logo)
your_card = []
dealer_card = []

def deal_card(your,dealer):
    while your >= 1:
        your_card.append(random.choice(cards))
        your-=1
    while dealer >=1:
        dealer_card.append(random.choice(cards))
        dealer-=1
    # print(f"Your cards are : {your_card}")
    # print(f"Dealers cards are : {dealer_card}")
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def start_game():
    end_game = False
    while end_game == False:
        deal_card(your=2,dealer=2)
        print(f"Cards you got : {your_card}, Your score is {sum(your_card)}")
        print(f"Cards that computer got : [{dealer_card[0]},?]")
        while sum(dealer_card) < 17:
            deal_card(your=0,dealer=1)
        if input("Press y to hit again, press any other key to stand : ").lower() == "y":
            deal_card(your=1,dealer=0)
            print(f"Cards you got : {your_card}, Your score is {sum(your_card)}")
            print(f"Your score is : {sum(your_card)}")
            print(f"Dealers score is : {sum(dealer_card)}")
        if (sum(your_card) <= 21 and sum(dealer_card) < sum(your_card)) or (sum(your_card) <= 21 and sum(dealer_card) > 21):
            print("You win")
            print(f"Your score is : {sum(your_card)}")
            print(f"Dealers score is : {sum(dealer_card)}")
        elif(sum(your_card) < sum(dealer_card) and sum(dealer_card) <= 21) or (sum(your_card) > sum(dealer_card) and sum(dealer_card) <= 21):
            print("You lose")
            print(f"Your score is : {sum(your_card)}")
            print(f"Dealers score is : {sum(dealer_card)}")
        elif sum(your_card) == sum(dealer_card):
            print("Draw")
            print(f"Your score is : {sum(your_card)}")
            print(f"Dealers score is : {sum(dealer_card)}")

        option = input("press c to continue the game ,press q to quit, press y to restart the game : ").lower()  
        if option == "q":
            end_game = True
        elif option == "y":
            your_card.clear()
            dealer_card.clear()
            start_game()
        else:
            print(f"Invalid option {option}")

start_game()
