MENU = {
    "espresso":{
        "ingredients":{
            "water":50,
            "coffee":18,
        },
        "cost":1.5,
    },

    "latte":{
        "ingredients":{
            "water":200,
            "milk": 150,
            "coffee":24,
        },
        "cost":2.5,
    },

    "cappuccino":{
        "ingredients":{
            "water":250,
            "milk": 100,
            "coffee":24,
        },
        "cost":2.5,
    },

}

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    

}


def check_resources(beverage):
    #print(beverage)
    print(beverage['ingredients'])

    for item in beverage['ingredients']:

        if beverage['ingredients'][item]> resources [item]:
            print("Not enough resources")
            return False

    #print("enough resources")
    return True 
        

def process_coins():

    print("insert coins: ")
    quarter = int(input("How many quarters do you have?"))
    dime = int(input("How many dimes do you have?"))
    nickel = int(input("How many nickels do you have?"))
    penny = int(input("How many pennies do you have?"))
    
    money = 0.25*quarter + 0.10*dime + nickel*0.05 + penny * 0.01

    return money


def transaction_status(money_received, drink_cost):

    global profit

    if money_received >= drink_cost:
        change = (money_received - drink_cost, 2)
        profit += drink_cost
        print(f"The profit is: {profit}")
        return True

    else:
        print("Sorry not enough money. Money refunded.")
        return False
    

def make_coffee(drink_name, order_ingredients):
    
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]

    print(f"Here is your {drink_name}!")
    print(resources)



continuation = True

while continuation:

    pick = input("What do you want to drink? (latte, cappuccino or espresso) ")

    if pick == "off":
        continuation = False

    elif pick == "report":
        print(resources)

    else:
        drink = MENU[pick]
        if check_resources(drink):
        #check_resources(pick['ingredients'])
            payment = process_coins()
            if transaction_status(payment, drink['cost']):
                make_coffee(pick, drink['ingredients'])

        
