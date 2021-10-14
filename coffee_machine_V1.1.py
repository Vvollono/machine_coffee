from database import MENU, coins, resources


# TODO.3 Improve function payment using a dictionary for the coin
def payment(coins, MENU, total_coins):
    """Returns the total of the coins inserted and check if the user insert enough money"""
    for coin in coins:
        coin_insert = int(input(f"How many {coin}: "))
        coin_insert *= coins[coin]
        total_coins += coin_insert
        print(total_coins)
    # TODO.4 make a check if the user insert the right amount if is more give change else tell the user is not enought
    if total_coins >= MENU["cost"]:
        print("Here is your drink enjoy!!")
        profit = total_coins
        if total_coins > MENU["cost"]:
            change = round(total_coins - MENU["cost"], 2)
            print(f"You're change : {change}")
            profit = total_coins - change
    else:
        print(f"You insert {total_coins}, the prize is {MENU['cost']}\n I give back your money")
        profit = 0
        return profit
    return profit


# TODO.2 Improve function resource check


def resources_check(MENU, order, resources):
    """Check if is enough ingredients in the coffee machine and returns True if is sufficient or False if not"""
    global check
    for i in resources:
        if i in MENU[order]["ingredients"]:
            if resources[i] < MENU[order]["ingredients"][i]:
                
                print(f"Sorry there is not enough {i}")
                check = False
                return check
            elif resources[i] >= MENU[order]["ingredients"][i]:
                check = True
    return check


# TODO.1 Change code with an in loop for the order program
total_coins = 0
money = 0
on = True
while on:
    order = input("What do you like? espresso, latte, cappuccino,tea,prize: ").lower()
    if order == "report":
        print(f"Water: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}\nTea Bags: "
              f"{resources['tea_bag']}\nMoney:$ {money}")
    elif order == "off":
        on = False
    elif order == "price":
        print("Espresso price:$", MENU["espresso"]["cost"], "\n", "Latte price:$", MENU["latte"]["cost"], "\n",
              "Cappuccino price:$", MENU["cappuccino"]["cost"], "\n","Tea price:$", MENU["tea"]["cost"])
    for drink in MENU:
        if drink in order:
            is_enough = resources_check(MENU, order, resources)
            if is_enough:
                for ingr in resources:
                    if ingr in MENU[order]["ingredients"]:
                        resources[ingr] -= MENU[order]["ingredients"][ingr]
            money_in = payment(coins, MENU[drink], total_coins)
            money += money_in

