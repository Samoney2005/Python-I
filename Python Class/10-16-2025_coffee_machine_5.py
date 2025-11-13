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
# What would you like?

#function declaration

def resources_sufficient(beverage):


    for item in beverage['ingredients']:
       #print(item)
        print(beverage['ingredients'][item])
        print(f"The value for the resources is {resources[item]}")

        
        if resources[item] < beverage['ingredients'][item]:
            
            print(f'Sorry we are out of {item}.')
            return False


    print(f'We have enough {item}!')   
    return True      




# process coins
def process_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.10
    nickels = int(input("How many nickels?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01
    payment = quarters + dimes + nickels + pennies
    return payment


# check transaction
def check_transact(payment):
    global profit 
    if payment >= drink["cost"]:
        change = round(payment - drink["cost"], 2)
        print("You have enough money!")
        if change > 0:
            print(f"Here is ${change} in change.")
            
            profit += drink["cost"]
        return True 
    
   
    else:
        print("You dont have enough money!")
        return False


# 3. Make Coffee (Deduct Resources)
def make_coffee():
    for item in drink["ingredients"]:
        if resources[item] < drink["ingredients"][item]:



            resources[item] -= drink["ingredients"][item]
            print(f"Here is your {choice} Enjoy!")
        ret

        else:
            print("Not enough ingredients.")











continuation = True

while continuation:
    choice = input("What would you like?(espresso/latte/cappuccino)")
    print(choice)
    
# The coffee machine is now off
    if choice == "off":
        continuation = False

# Print the report of avaliable resources
    elif choice == "report":
        print(resources)
        print(f'The profit is:{profit}')
        
# Check resources sufficient?
    else:

        drink = MENU[choice]

        if resources_sufficient(drink)== True:
            coin = process_coins()
            check_transact(coin)
        #print(MENU[choice]["ingredients"]["water"])
        
    

# Process coins









    '''

        drink = MENU.get(choice)
        if drink and resources_sufficient(drink["ingredients"]):
            # 1. Process Coins
            print("Please insert coins.")
            quarters = int(input("How many quarters?: ")) * 0.25
            dimes = int(input("How many dimes?: ")) * 0.10
            nickels = int(input("How many nickels?: ")) * 0.05
            pennies = int(input("How many pennies?: ")) * 0.01
            payment = quarters + dimes + nickels + pennies

            # 2. Check Transaction
            if payment >= drink["cost"]:
                change = round(payment - drink["cost"], 2)
                if change > 0:
                    print(f"Here is ${change} in change.")
                
                profit += drink["cost"]
                
                # 3. Make Coffee (Deduct Resources)
                for item in drink["ingredients"]:
                    resources[item] -= drink["ingredients"][item]
                print(f"Here is your {choice} Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")

    '''


print(f'The coffee machine is now off')



#print(MENU['latte']['ingredients']['water'])
