import random
from Hangman_game.hang_man_art import *
from Hangman_game.word_list import word_list
empty_list = []


random_word = random.choice(word_list)


def replace_blanks(character):
    # print(f'index of character is {random_word.index(character)}')
    if character in empty_list:
        print(f'You have already guessed the letter : {character}')
    else:
        for i in range(len(random_word)):
             if character == random_word[i]:
                empty_list[i] = character

    return


for i in range(len(random_word)):
    empty_list.append('_')

end_of_game = False
lives = 5
print(logo)
print("Welcome to the game")
while end_of_game != True:

    character = input("Guess the letter: ").lower()
    
    for char in random_word:
        if char == character:
            replace_blanks(char)
    
    if character not in random_word:
        print(f"{character} is not in the word")
        hangman = stages.__getitem__(lives)
        print(hangman)
        lives -= 1  

    print(f"{' '.join(empty_list)}")
    if lives < 0:
        end_of_game = True
        print(f'Sorry you lost')
    if '_' not in empty_list:
        end_of_game = True
        print(f'You have won!! Congradulations!!')

