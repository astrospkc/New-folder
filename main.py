MENU = {
    "espresso": {
        "ingredients": {
            "milk": 0,
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
price = 0

# money = {
#     "quarters": 0.25,
#     "dimes": 0.10,
#     "nickles": 0.05,
#     "pennies": 0.01
# }


def resource_sufficient(ingredient):
    """return true when order can be made. False when it can't be done"""
    for item in ingredient:
        if ingredient[item] > resources[item]:
            print(
                f"Sorry , order can't be placed due to shortage of ingredients {item}.")
            return False
        return True


def process_coins():
    """returns the total coins"""
    print("Please insert your coins.")
    total = int(input("how many quarter? : "))*0.25 + int(input("how many dimes? : ")) * \
        0.1 + int(input("how many nickles? : "))*0.05 + \
        int(input("how many pennies? : "))*0.01
    return total


def transation_process(money_received, drink_cost):
    "returns true if ney received is successful , false if insufficient"
    if money_received >= drink_cost:
        change = round((money_received - drink_cost), 2)
        print(f"Here is your {change} change.")
        global price
        price += drink_cost
        return True
    else:
        print("Sorry , insufficient amount, money is refunded.")
        return False


def drinks(drink_name, ingredient):
    "Deduct the ingredients from the ordered drink"
    for item in ingredient:
        resources[item] -= ingredient[item]
    print(f"Here is your {drink_name}. Enjoy!")


is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino):")
    if choice == "off":
        is_on = False

    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${price}")

    else:
        drink = MENU[choice]
        if resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if transation_process(payment, drink["cost"]):
                drinks(choice, drink["ingredients"])
