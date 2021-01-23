from Day_15_Data import resources,MENU
import math
profit = 0
def is_enough_resources(drink_ingredients):
    is_available = True
    for item in drink_ingredients:
        if drink_ingredients[item] >= resources[item]:
            print(f'Sorry there is not enough {item}.')
            is_available =  False
    return is_available

def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Cost: {profit}")

def process_coins():
    total = int(input('How many Quarters? ')) * 0.25
    total += int(input('how many Dimes? ')) * 0.1
    total += int(input('How many nickles? ')) * 0.05
    total += int(input('How many Pennies? ')) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        global profit
        change = round(money_received - drink_cost, 2)
        print(f'Here is your ${change} change ')
        profit += drink_cost
        return True
    else:
        print('Not enough money.🚨 Money refunded')
        return False

def make_coffe(choice, ingredients):
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f'Here is your {choice} Coffee ☕')
is_on = True

while is_on:
    choice = input('What would you like? (espresso/latte/cappuccino): ')
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        report()
    else:
        drink = MENU[choice]
        if is_enough_resources(drink['ingredients']):
            payment = process_coins() 
            if is_transaction_successful(payment, drink['cost']):
                make_cofee(choice, drink['ingredients'])

    