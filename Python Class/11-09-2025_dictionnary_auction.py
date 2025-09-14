# declare Variable
bid_log = {}  #declare a dictionnary
print(bid_log)
#bid_log = {name:bid}

# "What is your name?","What is your bid?"

var = True

while var:
    name = input("What is your name?")
    bid = input("What is your bid?")


    bid_log[name] = bid
    print(bid_log)
    
    # if yes continue, no exit loop
    follow = input("Do you want to continue? Yes or No?")

    if follow == "yes":
        print("I will continue!")
        
    elif follow == "no":
        var = False
        
# Compare who got the highest bid
if bid >= "10000":
    print(f'You won the auction, Congrats!')
    


    
