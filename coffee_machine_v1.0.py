MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def payment(MENU):
    """ask the user to insert coin shows the actual amount and verify if is enough for the drink"""
    total_coins = 0
    quarter = 0.25
    dime = 0.10
    nikel = 0.05
    penny = 0.01
    price_product = MENU["cost"]
    print("Please insert coins")
    quarter_insert = int(input("How many quarters: "))
    total_quarter = quarter_insert * quarter
    total_coins += total_quarter
    print(f"The total insert is {total_coins}")
    dime_insert = int(input("How many dimes: "))
    total_dimes = dime_insert * dime
    total_coins += total_dimes
    print(f"The total insert is {total_coins}")
    nikel_insert = int(input("How many nikel: "))
    total_nikel = nikel_insert * nikel
    total_coins += total_nikel
    print(f"The total insert is {total_coins}")
    penny_insert = int(input("How many penny: "))
    total_penny = penny_insert * penny
    total_coins += total_penny
    print(f"The total insert is {total_coins}")
    if total_coins >= MENU["cost"]:
        print("Here is your drink enjoy!!")
        if total_coins > MENU["cost"]:
            change = round(total_coins - MENU["cost"], 2)
            print(f"You're change : {change}")
            profit = total_coins - change
            return profit
    else:
        print(f"You insert {total_coins}, the prize is {price_product}\n I give back your money")
        profit = 0
        return profit


def resources_check(water, milk, coffee, MENU):
    """Check if is enough ingredients in the coffee machine"""
    if water < MENU["ingredients"]["water"]:
        print("Sorry there is not enough water")
        check = False
        return check
    elif coffee < MENU["ingredients"]["coffee"]:
        print("Sorry there is not enough coffee")
        check = False
        return check
    elif milk < MENU["ingredients"]["milk"]:
        print("Sorry there is not enough coffee")
        check = False
        return check
    else:
        check = True
        return check

water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]
money = 0
on = True
while on:
    order = input("What do you like? espresso, latte, cappuccino,prize: ").lower()
    # TODO print the report

    if order == "report":
        print(f"Water: {water}\nMilk: {milk} \nCoffee: {coffee}\nMoney:$ {money}")
    elif order == "off":
        on = False
    elif order == "price":
        print("Espresso price:$", MENU["espresso"]["cost"], "\n", "Latte price:$", MENU["latte"]["cost"], "\n",
              "Cappuccino price:$", MENU["cappuccino"]["cost"])
    elif order == "espresso":
        is_enough = resources_check(water, milk, coffee, MENU["espresso"])
        if is_enough:
            water -= MENU["espresso"]["ingredients"]["water"]
            coffee -= MENU["espresso"]["ingredients"]["coffee"]
            money_es = payment(MENU["espresso"])
            money += money_es
    elif order == "latte":
        is_enough = resources_check(water, milk, coffee, MENU["latte"])
        if is_enough:
            water -= MENU["latte"]["ingredients"]["water"]
            milk -= MENU["latte"]["ingredients"]["milk"]
            coffee -= MENU["latte"]["ingredients"]["coffee"]
            money_la = payment(MENU["latte"])
            money += money_la
    elif order == "cappuccino":
        is_enough = resources_check(water, milk, coffee, MENU["cappuccino"])
        if is_enough:
            water -= MENU["cappuccino"]["ingredients"]["water"]
            milk -= MENU["cappuccino"]["ingredients"]["milk"]
            coffee -= MENU["cappuccino"]["ingredients"]["coffee"]
            money_cap = payment(MENU["cappuccino"])
            money += money_cap


