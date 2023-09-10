# 5. Process coins.
# 6. Check transaction successful?
# 7. Make Coffee.

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
available_drinks = menu.get_items()
# requested_drink = menu.find_drink("latte")


machine_on = True
while machine_on == True:
    user_input = input("What would you like? " + available_drinks + ": ")
    if user_input == "off":
        machine_on = False
    elif user_input == "report":
        print(coffee_maker.report())
        print(money_machine.report())
    elif user_input in menu.get_items():
        requested_drink = menu.find_drink(user_input)
        drink_name = requested_drink.name
        drink_price = requested_drink.cost
        drink_ingredients = requested_drink.ingredients
        if coffee_maker.is_resource_sufficient(requested_drink):
            if money_machine.make_payment(drink_price):
                coffee_maker.make_coffee(requested_drink)
