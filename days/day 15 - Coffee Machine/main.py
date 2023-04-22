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

profit = 0
resources = {
    "water": 3000,
    "milk": 2000,
    "coffee": 1000,
}

in_process = True


def sufficient_resources(datas):
    for data in datas:
        if resources[data] < datas[data]:
            print(f"Sorry there is not enough {data}.”")
            return False
        else:
            return True


def is_transaction_successful(input_price, drink_price):
    """Return True when the payment is accepted, or False if money is insufficient."""
    print(drink_price, input_price)

    if input_price >= drink_price:
        change = round(input_price - drink_price, 2)
        if change > 0:
            print(f"Here is ${change} dollars in change.")
        global profit
        profit += drink_price
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def deduct_ingredients(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


while in_process:
    coffee_name: str = input("What would you like? (espresso/latte/cappuccino): ")
    if coffee_name == "off":
        in_process = False
    elif coffee_name == "report":
        print(f"water: {resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print(f"coffee: {resources['coffee']}g")
        print(f"profit: ${profit}")
    elif any(any_name in coffee_name for any_name in MENU):
        chosen_drink = MENU[coffee_name]
        if sufficient_resources(chosen_drink["ingredients"]):
            quarters = 0
            while True:
                quarters_input = input("How many quarters? ").strip()
                if quarters_input.isdigit():
                    quarters = int(quarters_input)
                    break
                else:
                    print("Please enter a valid natural number.")

            dimes = 0
            while True:
                dimes_input = input("How many dimes? ").strip()
                if dimes_input.isdigit():
                    dimes = int(dimes_input)
                    break
                else:
                    print("Please enter a valid natural number.")

            nickels = 0
            while True:
                nickels_input = input("How many nickels? ").strip()
                if nickels_input.isdigit():
                    nickels = int(nickels_input)
                    break
                else:
                    print("Please enter a valid natural number.")

            pennies = 0
            while True:
                pennies_input = input("How many pennies? ").strip()
                if pennies_input.isdigit():
                    pennies = int(pennies_input)
                    break
                else:
                    print("Please enter a valid natural number.")

            coins = quarters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01

            if is_transaction_successful(coins, chosen_drink["cost"]):
                deduct_ingredients(coffee_name, chosen_drink["ingredients"])
    else:
        print("no such option, please select correct one")
