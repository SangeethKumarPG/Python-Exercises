from art import *
from game_data import data
import random
import os

score = 0

def high_or_low(first_choice, second_choice):
    if first_choice != second_choice:
        print(logo)
        print(f"Your current score is {score}")
        print(f"Comapare A: {first_choice['name']} a {first_choice['description']} , from {first_choice['country']}")
        print(vs)
        print(f"Against B: {second_choice['name']} a {second_choice['description']} , from {second_choice['country']}")
        option = input()
        if option == 'a':
            if first_choice['follower_count'] > second_choice['follower_count']:
                print(f"Correct")
                return 1
            else:
                print("Incorrect")
                return 0
        elif option == "b":
            if first_choice['follower_count'] < second_choice['follower_count']:
                print(f"Correct")
                return 1
            else:
                print("Incorrect")
                return 0
    else:
        return 2
            
end_game = False
first_choice = random.choice(data)
second_choice = random.choice(data)
while end_game != True:
    # for item in first_choice:
    #     print(f"First choice : {item}")
    result = high_or_low(first_choice, second_choice)
    if result == 0:
        print(f"Your score is {score}.better luck next time ")
        end_game = True
    elif result == 1:
        score += 1
        first_choice = second_choice
        second_choice = random.choice(data)
        os.system('clear')
    elif result == 2:
        first_choice = random.choice(data)
        second_choice = random.choice(data)


    