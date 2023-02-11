MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
MONEY = 0.0
def has_coffee_and_water(has_coffee,has_water):
    if has_coffee and has_water:
        return "OK"
    elif has_coffee == False and has_water == True:
        return "Don't have enough coffee"
    elif has_coffee == True and has_water == False:
        return "Don't have enough water"
    else:
        return "Don't have enough coffee and water"
        
def is_resorce_sufficient(item):
    required_resource = MENU[item]['ingredients']
    has_water = False
    has_milk = False
    has_coffee = False
    if resources["water"] - required_resource['water'] >= 0:
        has_water = True
    if 'milk' in required_resource:
        if resources["water"] - required_resource['water'] >= 0:
            has_milk = True
    if resources["coffee"] - required_resource['coffee'] >= 0:
        has_coffee = True
    if 'milk' in required_resource and has_milk:
        return has_coffee_and_water(has_coffee, has_water)
    elif 'milk' in required_resource and has_milk == False:
        return "Don't have enough milk"
    else:
        return has_coffee_and_water(has_coffee, has_water)
    
def has_enough_money(choice):
    global MONEY
    quarter = int(input("Insert the quarters : "))
    dime = int(input("Insert the dimes : "))
    nickel = int(input("Insert the nickels : "))
    pennies = int(input("Insert the pennies : "))
    total_amount = (0.25 * quarter) + (0.10 * dime) + (0.05 * nickel) + (0.01 * pennies)
    inserted_money = round(total_amount,2)
    if MENU[choice]['cost'] > inserted_money:
        print(f"Not enough money ! You need ${round((MENU[choice]['cost'] - inserted_money),2)} more.") 
        print(f"You have inserted {inserted_money}")
        print(f"Refunding the inserted amount of ${inserted_money}")
        return False
    elif MENU[choice]['cost'] < inserted_money:
        excess_amount = round((inserted_money - MENU[choice]['cost']),2)
        print(f"You have inserted ${inserted_money}")
        print(f"Refunding excess amount of {excess_amount}")
        MONEY = MONEY + (inserted_money - excess_amount)
        return True
    elif MENU[choice]['cost'] == inserted_money:
        MONEY += inserted_money
        print(f"You have inserted $ {inserted_money}")
        return True
    else:
        return False
    
def make_coffee(choice):
    ingredients = MENU[choice]['ingredients']
    resources["coffee"] = resources["coffee"] - ingredients["coffee"]
    resources["water"] = resources["water"] - ingredients["water"]
    if 'milk' in ingredients:
        resources["milk"] = resources["milk"] - ingredients["milk"]
    print(f"Here is your {choice} ☕️ enjoy")

power_on = True
while power_on:
    choice = input("What would you like (espresso/latte/cappuccino)")
    if choice.lower() == "report":
        print(f"water : {resources['water']}")
        print(f"milk : {resources['milk']}")
        print(f"coffee : {resources['coffee']}")
        print(f"money : ${MONEY}")
    elif choice.lower() == "off":
        power_on = False
    elif choice.lower() == "espresso":
        resource_sufficient = is_resorce_sufficient("espresso") 
        if resource_sufficient == "OK":
            if has_enough_money(choice.lower()):
                make_coffee("espresso")
            else:
                print(f"Bye!!")
        else:
            print(f"Resource not sufficient : {resource_sufficient}")
    elif choice.lower() == "latte":
        resource_sufficient = is_resorce_sufficient("latte") 
        if resource_sufficient == "OK":
            if has_enough_money(choice.lower()):
                make_coffee("latte")
            else:
                print(f"Bye!!")
        else:
            print(f"Resource not sufficient : {resource_sufficient}")
    elif choice.lower() == "cappuccino":
        resource_sufficient = is_resorce_sufficient("cappuccino") 
        if resource_sufficient == "OK":
            if has_enough_money(choice.lower()):
                make_coffee("cappuccino")
            else:
                print(f"Bye!!")
        else:
            print(f"Resource not sufficient : {resource_sufficient}")
    else:
        print(f"Invalid choice {choice}")

            
