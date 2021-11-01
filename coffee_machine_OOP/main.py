from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menup = Menu()
maker_coffee = CoffeeMaker()
money = MoneyMachine()

def machine():
    print("### Price List ### \nespresso: $1.5 ;  latte: $2.5 ;  cappuccino: $3.0 \n")
    coffee = input("What would you like? (espresso/latte/cappuccino): ")
    # print(make_coffee.report())
    if coffee == "report":
        maker_coffee.report()
        money.report()
        machine()
    else:
        drink = menup.find_drink(coffee)
        can_make = (maker_coffee.is_resource_sufficient(drink))
        if can_make:
            money.make_payment(drink.cost)
            maker_coffee.make_coffee(drink)
            machine()
        else:
            print("ingredients are insufficient")
            machine()
machine()