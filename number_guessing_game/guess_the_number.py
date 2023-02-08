import random
from art import logo
print(logo)
number = random.randint(1,100)
level = {
    'easy':10,
    'hard' : 5
}
end_game = False
number_of_chances = 0
def guess_the_number(n):
    if n == number:
        print(f"Correct! The number is {number}")
        return 0
    elif n > number:
        print("Too high")
        return 1
    else :
        print("Too low")
        return -1

while end_game == False:
    difficulty = int(input("Choose the difficulty, type 1 for easy, type 2 for hard : "))
    if difficulty == 1:
        number_of_chances = level['easy']
    elif difficulty == 2:
        number_of_chances = level['hard']
    else:
        print(f"Invalid option {difficulty}")
    while number_of_chances > 0:
        guess = int(input("Enter your guess : "))
        success = guess_the_number(guess)
        number_of_chances -= 1
        if success == 0:
            end_game = True
            print(f"You have {number_of_chances} remaining chances")
            number_of_chances = 0
        else:
            print(f"You have {number_of_chances} remaining chances")

    if number_of_chances == 0 and success != 0:
        if success !=0:
            print("You lost. Press any key to continue. Press q to quit")
            if input().lower == "q":
                end_game = True
        else:
            print("Press any key to continue playing. Press q to quit")
            if input().lower == "q":
                end_game = True

        

