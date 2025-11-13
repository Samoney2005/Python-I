# declare Variable
bid_log = {}  #declare a dictionnary
print(bid_log)
max_bid = 0
max_name = ""

#bid_log = {name:bid}

# "What is your name?","What is your bid?"

var = True

while var:
    name = input("What is your name?")
    bid = int(input("What is your bid?"))


    bid_log[name] = bid
    print(bid_log)
    
    # if yes continue, no exit loop
    follow = input("Do you want to continue? Yes or No?")

    if follow.lower() == "yes":
        print("I will continue!")
        
    elif follow.lower() == "no":
        var = False


# "Who has the biggest bid?"
for obj in bid_log:
    print(bid_log[obj])

    if bid_log[obj] > max_bid:
        max_bid = bid_log[obj]
print(f'{name} is the max bid!') 
        
    

'''      
# Compare who got the highest bid
if bid >= "10000":
    print(f'You won the auction, Congrats!')   
'''

    
