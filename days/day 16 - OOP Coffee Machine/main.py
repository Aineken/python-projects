from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True


while is_on:
    options = menu.get_items()
    coffee_name: str = input(f"What would you like? {options}: ")
    if coffee_name == "off":
        print("thank you, bye bye :)")
        is_on = False
    elif coffee_name == "report":
        coffee_maker.report()
        money_machine.report()
    elif any(any_name in coffee_name for any_name in menu.get_names()):
        chosen_drink = menu.find_drink(coffee_name)
        if coffee_maker.is_resource_sufficient(chosen_drink) and money_machine.make_payment(chosen_drink.cost):
            coffee_maker.make_coffee(chosen_drink)
    else:
        print("no such option, please select correct one")

