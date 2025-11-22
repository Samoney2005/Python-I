#What was the bill?
bill = int(input("What was the bill?"))
#How much tip would you like to give? 10, 12 or 15 %?
tip = int(input("How much tip would you like to give?"))
#How many people will split the bill?
people = int(input("How many people will split the bill?"))
#Each person will pay: $...
pay = ("Each person will pay:")

conversion = (bill*(tip/100)/people)
print("Each person will pay:",conversion)

# Add check in conversion
# (bill*(1+tip)/100)/people)

