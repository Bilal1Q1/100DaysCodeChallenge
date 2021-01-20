MENU = {
    'espresso':{
        'ingredients' : {
            'water' : 50,
            'coffee' : 18
        },
        'cost' : 1.5
    },
    'latte':{
        'ingredients':{
            'water' : 200,
            'coffee' : 24,
            'milk' : 150
        },
        'cost' : 2.5
    },
    'cappuccino':{
        'ingredients':{
            'water' : 250,
            'coffee' : 24,
            'milk' : 100
        },
        'cost' : 3.
    }
}
def is_resources_sufficient(order_ingredients):
    
profit = 0
resources = {
    'water': 300,
    'milk' : 200,
    'coffee' : 100
}
is_on = True
choice = input('What would you like? (espresso/latte/cappuccino): ')
if choice == 'off':
    is_on = False
elif choice == 'report':
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Cost: {profit}")
else:
    drink = MENU[choice]
    is_resources_sufficient(drink['ingredients'])