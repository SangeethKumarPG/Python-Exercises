from art import *
import random
print(logo)
#list in dicionary

item_list = [
    {"apple": 1000000},
    {"cat videoes": 1500000},
    {"sunny leone" : 2000000},
    {"fake news": 450000},
    {"Chadwick Boseman": 3000000},
    {"Narendra Modi": 2500000},
    {"Edappal":2500},
    {"Lulu Mall":30000},
    {"Pinarayi":100000},
    {"Sony":150000}
]
def high_or_low(first_choice, second_choice):
    if first_choice != second_choice:
        for item in first_choice:
            print(f"First choice : {item}")
        for item_2 in second_choice:
            print(f"Second item : {item_2}")
        print("Press a for higher b for lower : ")
        option = input()
        if option == 'a':
            if first_choice[item] > second_choice[item_2]:
                print(f"Correct")
                return 1
            else:
                print("Incorrect")
                return 0
        elif option == "b":
            if first_choice[item] < second_choice[item_2]:
                print(f"Correct")
                return 1
            else:
                print("Incorrect")
                return 0

first_choice = random.choice(item_list)
second_choice = random.choice(item_list)
# for item in first_choice:
#     print(f"First choice : {item}")


high_or_low(first_choice, second_choice)