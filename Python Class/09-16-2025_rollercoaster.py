# declare Variable
ride_log = {}  # declare a dictionary to store rider's info

# "What is your name?","What is your height?","What is your age?"
check_riders = True

while check_riders:
    name = input("What is your name? ")
    height = int(input("What is your height in cm? "))
    age = int(input("What is your age? "))
    
    can_ride = False
    cost = 0

    if height > 120:
        can_ride = True
        if age < 12:
            cost = 5
        elif age <= 18:
            cost = 7
        else:
            cost = 12
        
    # Store the rider's information and result in the dictionary
    ride_log[name] = {"height": height, "age": age, "can_ride": can_ride, "cost": cost}
    print(ride_log)

    # if yes continue, no exit loop
    follow = input("Do you want to check another person? Yes or No? ")

    if follow.lower() == "yes":
        print("Okay, let's check the next person!")
        
    elif follow.lower() == "no":
        check_riders = False
        
# Display a summary of all riders checked
print("\n--- Ride Summary ---")
for rider_name, rider_info in ride_log.items():
    if rider_info["can_ride"]:
        print(f"{rider_name}: Can ride. The cost is ${rider_info['cost']}.")
    else:
        print(f"{rider_name}: Cannot ride.")