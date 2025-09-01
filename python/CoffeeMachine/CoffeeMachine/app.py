info = {
    'Water': 400,
    'Milk': 350,
    'Coffee': 76,
    'Money': 2.5
}

Menu = {
    'ESPRESSO': {
        'Price': 1,
        'Water': 50,
        'Coffee': 18
    },
    'LATTE': {
        'Price': 1.75,
        'Water': 200,
        'Coffee': 24,
        'Milk': 150
    },
    'CAPPUCCINO': {
        'Price': 2.5,
        'Water': 250,
        'Coffee': 24,
        'Milk': 100
    }
}

def coin():
    print("Please insert coins.")
    pennies = int(input('How many pennies?: '))
    dimes = int(input('How many dimes?: '))
    nickels = int(input('How many nickels?: '))
    quarters = int(input('How many quarters?: '))
    total = pennies*0.01 + dimes*0.1 + nickels*0.05 + quarters*0.25
    return round(total, 2)

def check_resources(coffee_choice):
    for item in Menu[coffee_choice]:
        if item != 'Price':
            if info.get(item, 0) < Menu[coffee_choice][item]:
                print(f"Sorry, not enough {item}.")
                return False
    return True

while True:
    print(f"\nAvailable Money: ${info['Money']}")
    coffee = input("What would you like? (espresso/latte/cappuccino): ").upper()

    if coffee == 'OFF':
        print('Thank You')
        break
    elif coffee == 'REPORT':
        print(
            f'''Water: {info['Water']}ml
Milk: {info['Milk']}ml
Coffee: {info['Coffee']}g
Money: ${info['Money']}''')
    elif coffee in Menu:
        if not check_resources(coffee):
            continue
        money_inserted = coin()
        cost = Menu[coffee]['Price']
        if money_inserted < cost:
            print("Sorry, that's not enough money. Money refunded.")
            continue
        change = round(money_inserted - cost, 2)
        print(f"Here is your change: ${change}")
        print(f"Enjoy your {coffee.lower()}!")

        
        for item in Menu[coffee]:
            if item != 'Price':
                info[item] -= Menu[coffee][item]
        info['Money'] += cost
    else:
        print("Invalid input. Try again.")