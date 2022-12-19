# TODO:choose drink you like?
from main import MENU, money, resources


def left_resources():
    print(continue_order.left_water)
    waterLeft = continue_order.left_water
    milkLeft = continue_order.left_milk
    coffeeLeft = continue_order.left_coffee

    return waterLeft, milkLeft, coffeeLeft


# machine k pass kitna resources left hain
def check_resources(drink_choosen):

    # ab isme while loop lagega jb tk resources khtam nhi ho jata
    while left_resources.waterLeft >= MENU[drink_choosen]["ingredients"]["water"] and left_resources.milkLeft >= MENU[drink_choosen]["ingredients"]["milk"] and left_resources.coffeeLeft >= MENU[drink_choosen]["ingredients"]["coffee"]:
        left_resources.waterLeft -= MENU[drink_choosen]["ingredients"]["water"]
        left_resources.milkLeft -= MENU[drink_choosen]["ingredients"]["water"]
        left_resources.coffeeLeft -= MENU[drink_choosen]["ingredients"]["water"]

    print(f" water left in the machine : {left_resources.waterLeft} ml")
    print(f" Milk left in the machine : {left_resources.milkLeft} ml")
    print(f" Coffee left in the machine : {left_resources.coffeeLeft} ml")


# kitna coins de raha h
def amount_user_pay(drink_choosen):
    quarter_amount = int(input("How many qaurters? "))
    dimes_amount = int(input("How many dimes ? "))
    nickles_amount = int(input("How many nickles ? "))
    pennies_amount = int(input("How many pennies ? "))

    Totalmoney_user_pay = (quarter_amount * money["quarters"]) + (dimes_amount * money["dimes"]) + (
        nickles_amount * money["nickles"]) + (pennies_amount * money["pennies"])

    Total_change = Totalmoney_user_pay - MENU[drink_choosen]["cost"]
    total_change = round(Total_change, 2)
    print(f"Money you get back : {total_change}")


def continue_order():

    want_to_continue = True
    while want_to_continue:
        drink = input(
            "Which drink you would like to have ? (espresso/latte/ cappuccino)")

        continue_order.left_water = resources["water"] - \
            MENU[drink]["ingredients"]["water"]
        continue_order.left_milk = resources["milk"] - \
            MENU[drink]["ingredients"]["milk"]
        continue_order.left_coffee = resources["coffee"] - \
            MENU[drink]["ingredients"]["coffee"]

        left_resources()
        check_resources(drink)
        amount_user_pay(drink)


continue_order()
# def fun1():
#     fun1.var = 100
#     print(fun1.var)

# def fun2():
#     print(fun1.var)
