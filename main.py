from ingredients import MENU

# TODO: Implement a function to print the report
#   - Display current resource levels (water, milk, coffee, money)
def report():
    if drink_choice.lower() == "report":
        for item, quantity in MENU.resources.items():
            if item in ["water", "milk"]:
                print(f"{item} {quantity} ml")
            elif item == "coffee":
                print(f"{item} {quantity} g")
            else:
                print(f"{item} {quantity}")


# TODO: Create a function to display the prompt and get user input
#   - Implement a loop to keep the machine running until turned off
#   - Handle input for drink selection, "off", and "report"
def turn_off():
    """Secret process to turn off machine if user enters 'off' instead of beverage choice"""
    user_input = drink_choice

    if user_input.lower() == 'off':
        print("Goodbye!")
        exit()
    else:
        print("Application is still running.")


drink_names = list(MENU.keys())  # converts the keys in the MENU dictionary into drink names for easier reference

drink_choice = input(f"Welcome! What would you like to drink? Your choices are {', '.join(drink_names)}\n")


# TODO: Test the program thoroughly
#   - Create test cases for various scenarios (different drinks, insufficient resources, etc.)
#   - Verify that all requirements are met

report()
turn_off()


# TODO: Create a function to check if resources are sufficient
#   - Compare required ingredients with available resources
#   - Return True if sufficient, False otherwise

# TODO: Implement coin processing functionality
#   - Create a function to prompt for and calculate total money inserted
#   - Handle different coin values (quarters, dimes, nickels, pennies)

# TODO: Develop a function to check if the transaction is successful
#   - Compare money inserted with drink cost
#   - Handle scenarios for insufficient funds and excess payment (change)

# TODO: Create a function to make the coffee
#   - Deduct resources used for the selected drink
#   - Update the money in the machine
#   - Display success message to the user

# TODO: Implement main program logic
#   - Combine all functions into a cohesive program flow
#   - Ensure proper handling of all scenarios (resource check, payment, etc.)

# TODO: Add error handling and input validation
#   - Ensure the program can handle unexpected user inputs gracefully
