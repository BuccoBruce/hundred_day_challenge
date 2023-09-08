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

machine_off = False
money = 0.00


def prompt_user():
    request: str = input("What would you like? (espresso/latte/cappuccino): ")
    return request


def print_report():
    for resource, quantity in resources.items():
        if resource == "coffee":
            print(f"{resource.capitalize()}: {quantity}g")
        elif resource == "water" or resource == "milk":
            print(f"{resource.capitalize()}: {quantity}ml")
    print(f"Money: ${money}")


def check_resources(beverage):
    checker = 0

    for ingredient, quantity in MENU[beverage]["ingredients"].items():
        for liquid, amount in resources.items():
            if liquid == ingredient:
                if quantity > amount:
                    print(f"Sorry, there is not enough {liquid}")
                    checker += 1
    if checker == 0:
        return True
    else:
        return False


def validate_transaction(input_money, beverage):
    global money
    input_money = float(input_money)
    if input_money < MENU[beverage]["cost"]:
        print("Sorry, that's not enough money")
        return False
    elif input_money == MENU[beverage]["cost"]:
        money += round(input_money, 2)
        return True
    elif input_money > MENU[beverage]["cost"]:
        change = input_money - MENU[beverage]["cost"]
        change = float(round(change, 2))
        print(f"Here is ${change} in change.")
        money += round(input_money - change, 2)
        return True


def process_coins():
    print("Please insert coins.")
    quarters = float(input("How many quarters? "))
    dimes = float(input("How many dimes? "))
    nickels = float(input("How many nickels? "))
    pennies = float(input("How many pennies? "))
    total = ((quarters * 0.25) + (dimes * 0.1) + (nickels * 0.05) + (pennies * 0.01))
    return total


def make_coffee():
    global machine_off
    user_choice = prompt_user()
    if user_choice == "off":
        machine_off = True
    elif user_choice == "report":
        print_report()
    else:
        if check_resources(user_choice):
            input_money = process_coins()
            if validate_transaction(input_money, user_choice):
                print(f"Here is your {user_choice}, enjoy!")
                for menu_item, menu_quantity in MENU[user_choice]["ingredients"].items():
                    for resources_item, resources_quantity in resources.items():
                        if menu_item == resources_item:
                            resources[resources_item] -= MENU[user_choice]["ingredients"][menu_item]


while not machine_off:
    make_coffee()
