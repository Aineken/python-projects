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
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

in_process = True


def sufficient_resources(data):
    print(data)
    return True


while in_process:
    new: str = input("What would you like? (espresso/latte/cappuccino): ")
    if new == "off":
        in_process = False
    elif new == "report":
        print(f"water: {resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print(f"coffee: {resources['coffee']}g")
        print(f"profit: ${profit}")
    else:
        drink = MENU[new]
        if sufficient_resources(drink["ingredients"]):
            print("it worked")
