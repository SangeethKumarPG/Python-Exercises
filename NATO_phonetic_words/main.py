import pandas



phonetic_dict = {row.letter : row.code for (index,row) in pandas.read_csv("NATO_phonetic_words/nato_phonetic_alphabet.csv").iterrows()}

print(phonetic_dict)


word = input("Enter the word : ").upper()

# phonetic_code_word = [code for (letter,code) in phonetic_dict.items() if letter in word]
# phonetic_code_word = [value for letter in word for (key,value) in phonetic_dict.items() if letter in key]
phonetic_code_word = [phonetic_dict[code] for code in word if code in phonetic_dict]
print(phonetic_code_word)