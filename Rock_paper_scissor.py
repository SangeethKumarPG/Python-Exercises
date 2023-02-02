import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
option = int(input("Enter your choice, 0 for rock , 1 for paper, 2 for scissor"))
sign_list = ["rock","paper","scissor"]

if(option>= 0 and option<=2):
    computer_choice = random.choice(sign_list)
    if not sign_list[option] == computer_choice:
        if sign_list[option] == "rock" and computer_choice == "paper":
            print("You chose:")
            print(rock)
            print("computer chose:")
            print(paper)
            print("You lose")
        elif sign_list[option] == "rock" and computer_choice == "scissor":
            print("You chose:")
            print(rock)
            print("computer chose:")
            print(scissors)
            print("You win")
        elif sign_list[option] == "paper" and computer_choice == "rock":
            print("You chose:")
            print(paper)
            print("computer chose:")
            print(rock)
            print("You win")
        elif sign_list[option] == "paper" and computer_choice == "scissor":
            print("You chose:")
            print(paper)
            print("computer chose:")
            print(scissors)
            print("You lose")
        elif sign_list[option] == "scissor" and computer_choice == "rock":
            print("You chose:")
            print(scissors)
            print("computer chose:")
            print(rock)
            print("You lose")
        elif sign_list[option] == "scissor" and computer_choice == "paper":
            print("You chose:")
            print(scissors)
            print("computer chose:")
            print(paper)
            print("You win")