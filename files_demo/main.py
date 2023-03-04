file = open("text.txt")
content = file.read()
print(f" The conetent of the file is : {content}")
file.close()

# with open 

with open("text.txt") as file:
    new_content = file.read()
    print(f" The new content of the file from desktop is : {new_content}")


# Writing to file

with open("text.txt", mode="w") as file:
    text = "Hey this is a new content"
    file.write(text)

with open("text.txt") as file:
    new_content = file.read()
    print(f" The written content of the file is : {new_content}")

# #appending to file

with open("text.txt", mode="a") as file:
    appended_content = "\n new line"
    file.write(appended_content)

with open("text.txt") as file:
    new_content = file.read()
    print(f" The appended content of the file is : {new_content}")

#Writing content to desktop file(absolute path)

with open("/Users/sangeethkumarpg/Desktop/text.txt", mode="w") as file:
    file.write("\n this is a content that is being written to the desktop")
    
#Reading file from desktop(absolute file path)

with open("/Users/sangeethkumarpg/Desktop/text.txt") as file:
    print(f" The read content is : {file.read()}")

#opening file with relative path
with open("../../../text.txt") as file:
    print(f"The content of the file with relative path is :{file.read()}")
