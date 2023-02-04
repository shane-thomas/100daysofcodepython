from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

cm = CoffeeMaker()
m = Menu()
mm = MoneyMachine()

machine = True
while machine:
    options = m.get_items()
    prompt = input(f"What would you like? ({options}): ")
    if prompt == 'off':
        machine = False
    elif prompt == 'report':
        cm.report()
        mm.report()
    else:
        drink = m.find_drink(prompt)
        if cm.is_resource_sufficient(drink):
            if mm.make_payment(drink.cost):
                cm.make_coffee(drink)
