import ingredients

is_on = True                    # The coffee machine is on
funds = 2.50                    # Starting funds
resc = ingredients.resources    # Who needs to write all that?
menu = ingredients.menu         # Same.

def is_resource_sufficient(order_ingredients):
    """Use to check if the resources present in the machine are enough to make the user's drink choice"""
    for item in order_ingredients:
        if order_ingredients[item] >= resc[item]:
            print(f"\nSorry there is not enough {item}.\n")
            return False
        return True

def process_coins():
    """Returns the total calculated amount of coins inserted."""
    print("Please insert coins.")
    coin_total = 0
    coin_total += int(input("How many quarters?: ")) * 0.25
    coin_total += int(input("How many dimes?: ")) * 0.10
    coin_total += int(input("How many nickels?: ")) * 0.05
    coin_total += int(input("How many pennies?: ")) * 0.01
    return coin_total


def is_transaction_successful(money_received, drink_cost):
    """Return True if money_received is accepted, or False if money_received is insufficient"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Payment accepted! Here is your change: ${change}\n")
        global funds
        funds += drink_cost
        return True
    else:
        print("Sorry that is not enough money. Your money is refunded.\n")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct required ingredients from the resources"""
    for item in order_ingredients:
        resc[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}! Enjoy! ☕️ \n")


# The Coffee Machine is on!
while is_on:
    choice = input("\nWhat would you like to drink? (espresso/latte/cappuccino):\n")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"\nCurrent resources:\n "
              f"Water: {resc['water']} ml\n "
              f"Milk: {resc['milk']} ml\n "
              f"Coffee: {resc['coffee']} g")
        print(f"Current amount of money: ${funds}\n")
    elif choice not in menu:
        print("Sorry, that is not a valid drink choice. Please select again.\n")
    else:
        # Take user drink choice and check if the ingredients needed for that drink are available
        drink = menu[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(choice, drink['ingredients'])
                payment += funds
                another_choice = input("Would you like another drink? Y/N\n")
                if another_choice.lower() == 'y':
                    is_on = True
                elif another_choice.lower() == 'n':
                    is_on = False
                else:
                    print("Sorry, that is not a valid option.")
                    is_on = True
