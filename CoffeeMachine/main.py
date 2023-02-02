MENU = {
    "espresso": {
        "ingredients": {
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
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def process_coins():
    print("Please insert coins.")
    total = int(input("How many quarters? "))*0.25
    total += int(input("How many dimes? "))*0.1
    total += int(input("How many nickles? "))*0.05
    total += int(input("How many pennies? "))*0.01
    return total

def require(drink):
    for item in drink:
        if drink[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def transaction(money_recieved, drink_cost):
    global profit
    if money_recieved >= drink_cost:
        change = round(money_recieved - drink_cost,2)
        print(f"Here is %{change} in change.")
        profit+=drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False        

def make(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕")

machine = True
while machine:
    prompt = input("What would you like? (espresso/latte/cappuccino): ")
    if prompt == 'off':
        machine = False
    elif prompt == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[prompt]
        if require(drink["ingredients"]):
            payment = process_coins()
            if transaction(payment, drink["cost"]):
                make(prompt, drink["ingredients"])
