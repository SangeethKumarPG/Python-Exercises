from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)
quit = False
# def encrypt(text,shift):
#     encrpyted_text = []
#     # print(encrpyted_text)
#     for letter in text:
#         position = alphabet.index(letter)
#         if position + shift >=len(alphabet):
#             counter = 0
#             offset = 0
#             for i in range(position,len(alphabet)-1):
#                 counter+=1
#             offset = shift - counter
#             encrpyted_text.append(alphabet[offset-1])
#         else:
#             encrpyted_text.append(alphabet[position + shift])
#     print(f"Encrypted text is : {''.join(encrpyted_text)}")




# def decrypt(text,shift):
#     decrypted_text = []
#     for letter in text:
#         position = alphabet.index(letter)
#         if position - shift < 0:
#             counter = 0
#             offset = 0
#             for i in range(position,0,-1):
#                 counter+=1
#             offset = shift - counter
#             location = (len(alphabet) - 1) - offset
#             if location + 1 >25:
#                 location = 0
#             decrypted_text.append(alphabet[location+1])
#         else:
#             decrypted_text.append(alphabet[position-shift])
#     print(f"Decrypted text is {''.join(decrypted_text)}")

def ceaser(text,shift,direction):
    display_text = []
    if shift > 26:
        shift = int(shift % 26)

    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            if direction == 'encode':
                if position + shift >=len(alphabet):
                    counter = 0
                    offset = 0
                    for i in range(position,len(alphabet)-1):
                        counter+=1
                    offset = shift - counter
                    display_text.append(alphabet[offset-1])
                else:
                    display_text.append(alphabet[position + shift])
            else:
                if position - shift < 0:
                    counter = 0
                    offset = 0
                    for i in range(position,0,-1):
                        counter+=1
                    offset = shift - counter
                    location = (len(alphabet) - 1) - offset
                    if location + 1 >25:
                        location = 0
                    display_text.append(alphabet[location+1])
                else:
                    display_text.append(alphabet[position-shift])
        else:
            display_text.append(letter)
    
    print(f"{direction}d text : {''.join(display_text)}")



while quit != True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    ceaser(text=text,shift=shift,direction=direction)
    choice = input("Type yes to continue, type no to quit : ")
    if choice == "no":
        quit = True



# if direction == 'encode':
#     encrypt(text=text,shift=shift)
# elif direction == 'decode':
#     decrypt(text=text,shift=shift)
# else:
#     print("Enter a valid direction")