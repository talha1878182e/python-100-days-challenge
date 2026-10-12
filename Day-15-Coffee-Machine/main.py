MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 2.0,
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
    "water": 1000,
    "milk": 500,
    "coffee": 300,
}


def get_size_multiplier():
    while True:
        size = input("What size? (small/medium/large/xlarge): ").lower()
        if size == "small":
            return 1.0
        elif size == "medium":
            return 1.2
        elif size == "large":
            return 1.5
        elif size == "xlarge":
            return 1.8
        else:
            print("Invalid size choice. Please choose small, medium, or large.")


def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕. Enjoy!")


machine_is_on = True

while machine_is_on:
    choice = input("\nWhat would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "off":
        machine_is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    elif choice in MENU:
        multiplier = get_size_multiplier()
        base_drink = MENU[choice]

        scaled_ingredients = {
            item: round(amount * multiplier)
            for item, amount in base_drink["ingredients"].items()
        }
        scaled_cost = round(base_drink["cost"] * multiplier, 2)

        print(f"Total cost for {choice}: ${scaled_cost}")

        if is_resource_sufficient(scaled_ingredients):
            payment = process_coins()
            if is_transaction_successful(payment, scaled_cost):
                make_coffee(choice, scaled_ingredients)
    else:
        print("Invalid selection. Please choose espresso, latte, or cappuccino.")
