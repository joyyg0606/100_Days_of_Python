from menu_coffee_machine import resources, MENU
import art_coffee_machine

Money_in_machine = 0
enough_resources = True

def is_resource_enough():
    global enough_resources
    for ingrediant in MENU[user_choice]['ingredients']:
                if resources[ingrediant] < MENU[user_choice]['ingredients'][ingrediant]:
                    enough_resources = False
                    print(f"Sorry there is not enough {ingrediant}\n")
                    return
                
def calc_left_over_resources():
    for ingrediant in MENU[user_choice]['ingredients']:
        resources_left = resources[ingrediant] - MENU[user_choice]['ingredients'][ingrediant]
        resources[ingrediant] = resources_left
            
off = False
while off == False:
    print(art_coffee_machine.coffee_prices_art)
    user_choice = input("What would you like? [espresso / latte / cappuccino]: ").lower()

    if user_choice == 'off':
        off = True
    if user_choice == 'report':
        print(f"\nWater: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${Money_in_machine}\n")
    
    if user_choice == 'espresso' or user_choice == 'latte' or user_choice == 'cappuccino':
        is_resource_enough()

        if enough_resources == True:
            quarters = int(input("\nPlease insert coins.\nHow many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickles = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))
            total_amt = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)

            if MENU[user_choice]['cost'] > total_amt:
                print("\nSorry that's not enough money. Money refunded.\n")
            elif total_amt > MENU[user_choice]['cost']:
                calc_left_over_resources()
                Money_in_machine += MENU[user_choice]['cost']
                change = round((total_amt - MENU[user_choice]['cost']), 2)
                print(f"\nHere is ${change} in change.\nHere is your {user_choice} ☕ Enjoy!\n")
            else:
                calc_left_over_resources()
                Money_in_machine += MENU[user_choice]['cost']
                print(f"\nHere is your {user_choice} ☕ Enjoy!\n")