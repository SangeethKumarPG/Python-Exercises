#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("mail_merge/Input/Names/invited_names.txt") as data:
    names = data.readlines()


with open("mail_merge/Input/Letters/starting_letter.txt") as letter:
    content = letter.readlines()



final_letter_content = ""
for string in content:
    final_letter_content += string

for name in names:
    data = open(f"mail_merge/Output/ReadyToSend/letter_for_{name.strip()}", mode="w")
    names_changed_content = final_letter_content.replace("[name]",f"{name.strip()}")
    data.write(names_changed_content)
    data.close()

