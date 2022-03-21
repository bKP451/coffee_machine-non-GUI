from data import MENU, resources

money_collected = 0
end_machine = False


def display_resources(store):
    return f"""Water : {store['water']} ml
Milk  : {store['milk']} ml 
Coffee :{store['coffee']} g 
Money : ${money_collected}
"""


def check_for_resources(demand):
    water = MENU[demand]['ingredients']['water']
    coffee = MENU[demand]['ingredients']['coffee']
    water_av = resources['water']
    milk_av = resources['milk']
    coffee_av = resources['coffee']
    if demand != 'espresso':
        milk = MENU[demand]['ingredients']['milk']
        if water_av >= water and milk_av >= milk and coffee_av >= coffee:
            return True
        else:
            return False
    else:
        if water_av >= water and coffee_av >= coffee:
            return True
        else:
            return False


def edit_stock(price_to_be_added, drink_name):
    global money_collected
    resources['water'] -= MENU[drink_name]['ingredients']['water']
    resources['coffee'] -= MENU[drink_name]['ingredients']['coffee']
    if drink_name != "espresso":
        resources['milk'] = MENU[drink_name]['ingredients']['milk']
    money_collected += price_to_be_added


def handle_finance(price_, beverage_name):
    print("Please insert coins.")
    quarters = int(input("how many quarters ?:"))
    dimes = int(input("how many dimes ?:"))
    nickles = int(input("how many nickles ?:"))
    pennies = int(input("how many pennies ?:"))
    user_total = quarters*0.25 + dimes*0.1 + nickles*0.05 + pennies*0.01
    if user_total >= price:
        change = user_total - price_
        if change > 0:
            print(f"Here is your ${round(change,2)} in change")
        print(f"Here is your {beverage_name}. Enjoy")
        edit_stock(price_, beverage_name)
    else:
        print("Sorry Not sufficient amount !! Money refunded")


while not end_machine:
    # TODO 1. Print the resources when user gives input of "report"
    user_prompt = input("What would you like to have ? (espresso/latte/cappuccino): ").lower()
    if user_prompt == "report":
        print(display_resources(resources))
    elif user_prompt == "off":
        print("Have  a good  day. GOOD NIGHT. ")
        end_machine = True
    else:
        if user_prompt == "espresso" or user_prompt == 'latte' or user_prompt == 'cappuccino':

            # TODO 2 : I have to check whether resources are available for particular cup of tea
            # TODO 3 : I have to process the financial part
            # if check_for_resources(user_prompt):
            #     print(f"The price of {user_prompt} is $ {MENU[user_prompt]['cost']}")
            if check_for_resources(user_prompt):
                price = MENU[user_prompt]['cost']
                print(f"The price of {user_prompt} is {price}")
                handle_finance(price, user_prompt)
            else:
                print(f"SORRY. There are no resources for {user_prompt}")
        else:
            print(f"Enter again checking the spelling !!!")



