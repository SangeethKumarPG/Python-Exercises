import pandas



phonetic_dict = {row.letter : row.code for (index,row) in pandas.read_csv("exception_handling/NATO_phonetic_words/nato_phonetic_alphabet.csv").iterrows()}

print(phonetic_dict)

# while True:
#     # phonetic_code_word = [code for (letter,code) in phonetic_dict.items() if letter in word]
#     # phonetic_code_word = [value for letter in word for (key,value) in phonetic_dict.items() if letter in key]
#     word = input("Enter the word : ").upper()
#     try:
#         phonetic_code_word = [phonetic_dict[code] for code in word]
#     except KeyError:
#         print("Sorry only letters in alphabets allowed please try again")
#     else:
#         print(phonetic_code_word)
#         break

# alternative recommended method

def generate_phonetic():
    global phonetic_dict
    word = input("Enter the word : ").upper()
    try:
        phonetic_code_word = [phonetic_dict[code] for code in word]
    except KeyError:
        print("Sorry only letters in alphabets allowed please try again")
        generate_phonetic()
    else:
        print(phonetic_code_word)

generate_phonetic()