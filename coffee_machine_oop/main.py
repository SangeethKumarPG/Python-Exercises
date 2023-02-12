from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

power_on = True
while power_on:
    choice = input(f"Enter your choice {menu.get_items()}")
    if choice == "report":
        print(coffee_maker.report())
        print(money_machine.report())
    elif choice == "off":
        power_on = False
    elif menu.find_drink(choice) is not None:
        coffee = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(coffee):
            if money_machine.make_payment(coffee.cost):
                coffee_maker.make_coffee(coffee)
            

        