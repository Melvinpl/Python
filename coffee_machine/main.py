'''
report - to get remaining resource and money collected
off - to switch off Machine and load resources. 
'''


from data import MENU
from data import resources
from art import logo

resource_left = {"water": 1000,
                "milk": 1000,
                "coffee": 500,}
money_collected = 0

print(logo)
def machine():
    print("\n")
    print("### Price List ### \nespresso: $1.5 ;  latte: $2.5 ;  cappuccino: $3.0 \n")
    coffee = input("What would you like? (espresso/latte/cappuccino): ")

    def collect_money():
        print("Please insert coins.\n")
        quarters = int(input("how many quarters?: "))
        dimes= int(input("how many dimes?: "))
        nickle = int(input("how many nickle?: "))
        pennies = int(input("how many pennies?: "))
        total = (quarters * 0.25) + (dimes * 0.1) + (nickle * 0.05) + (pennies * 0.01)
        return total



    def make_coffee(coffee):
        global money_collected
        cost = float(MENU[coffee]["cost"])
        total = float(collect_money())
        if cost <= total :
            change = round(total - cost,2)
            print(f"Here is {change} in change.\n")
            print(f"Here is your {coffee} ☕️. Enjoy! \n")
            money_collected += cost
            resource_used(coffee)
        elif cost > total:
            print("Sorry that's not enough money. Money refunded.")

    def resource_used(coffee):
        global resource_left
        water = int(resource_left["water"]) 
        resource_left["water"] = water - int(MENU[coffee]["ingredients"]["water"])
        milk = int(resource_left["milk"]) 
        resource_left["milk"] = milk - int(MENU[coffee]["ingredients"]["milk"])
        cofee = int(resource_left["coffee"]) 
        resource_left["coffee"] = cofee - int(MENU[coffee]["ingredients"]["coffee"])

    def check(coffee):
        global resource_left
        water = int(resource_left["water"]) 
        milk = int(resource_left["milk"]) 
        cofee = int(resource_left["coffee"])
        water_i = int(MENU[coffee]["ingredients"]["water"])
        milk_i = int(MENU[coffee]["ingredients"]["milk"])
        coffee_i = int(MENU[coffee]["ingredients"]["coffee"])

        if (water >= water_i) and (milk >= milk_i) and (cofee >= coffee_i):
            return True
        else:
            return False

    if coffee == "report":
        for i in resource_left:
            print(f"{i} : {resource_left[i]}")
        print(f"Money : ${money_collected}")
        machine()
    if coffee == "espresso" or coffee == "latte" or coffee =="cappuccino":
        avalilable = check(coffee)
        if avalilable:
            make_coffee(coffee)
        else:
            print("Sorry there is not enough resource. Turn off machine and re-fill. Type 'report' to get resource list")
        machine()
    if coffee == "off":
        print("Switching off")


machine()
