from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

TURN_OFF = False
coffee_menu = Menu()
coffeemaker = CoffeeMaker()
moneymachine = MoneyMachine()

while not TURN_OFF:
    requested_drink_name = input(f"What would you like? ({coffee_menu.get_items()}): ")

    if requested_drink_name == "report":
        coffeemaker.report()
        moneymachine.report()
    elif requested_drink_name == "off":
        TURN_OFF = True
    else:
        requested_item = coffee_menu.find_drink(requested_drink_name)
        if coffeemaker.is_resource_sufficient(requested_item):
            moneymachine.make_payment(requested_item.cost)
            coffeemaker.make_coffee(requested_item)

