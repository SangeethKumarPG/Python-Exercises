file_path = "exception_handling/a_file.txt"
try:
    file = open(file_path,"r")
    my_dictionary = {"a" : "Value"}
    # print(my_dictionary["b"])
except FileNotFoundError:
    print("File not found creating a a new file")
    file = open(file_path, "w")
    file.write("\n something")
except KeyError as error_message:
    print(f"The key {error_message}does not exists in my_dictionary")
else:
    content = file.read()
    print(content)
finally:
    #close the file here
    # file.close()
    print("File was closed")