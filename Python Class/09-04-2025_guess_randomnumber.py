# Can you guess the random number?
import random
var = 0
                   
# random.randint
guess_number = random.randint(15,40)
print(f"The random number is{guess_number}")

# how many times will get to guess
while var < 6:
    type_number = int(input(" Enter your number guess:"))
    
# is the random number > or < than the guessed number
    if type_number > guess_number:
        print("type number is greater than guess number")
    elif type_number < guess_number:
        print("guess number is less than type number")
        
# if the random number = to the guessed number 
    else:
        print(" You have found the number!")

    var+=1
