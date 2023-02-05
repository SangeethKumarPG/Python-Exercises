from art import logo
print(logo)

def add(n1,n2):
    return n1 + n2
def subtract(n1,n2):
    return n1 - n2
def multiply(n1,n2):
    return n1 * n2
def divide(n1,n2):
    return n1 / n2
def calculator():
    exit_loop = False
    operations = {'+':add, '-':subtract,'*':multiply,'/':divide}
    num1 = float(input("What would be the first number? : "))
    while exit_loop != True:
        for key in operations:
            print(f'{key}')
        operation = input("Pick an operation from the line above : ")
        num2 = float(input("What would be the next number? :"))
        if operation in operations:
            result = operations[operation]
            answer = result(num1,num2)
            print(f'{num1} {operation} {num2} = {answer}')
            num1 = answer
        else:
            print(f"Invalid operator {operation}")
        option = input(f"Press any key to continue calculation with {answer} or press n to start a new calculator or press q to quit : ")
        if  option.lower() == "n":
            exit_loop = True
            calculator()
        elif option.lower() == "q":
            exit_loop = True
            print("Thank you")
        else:
            print(f"Inavlid option : {option}")

calculator()
        


