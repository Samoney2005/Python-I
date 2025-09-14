# Enter the number
number = int(input("Enter your integer: "))
'''Put if statment 
if number > 0:
    print("This number is positive!")
elif number < 0:
    print("This number is negative!")
else:
    print("Number is equal to zero")
'''

# if number between 0 and 4, display "number is between 0 and 4
if 0 <= number <= 4:

#if number<4 and number>0: 
    
     print("Number is between 0 and 4 or equal to 0 or 4")
     
# if number between 4 and 8, display "number is between 4 and 8

if 4 < number <= 8:
    print("Number is between 4 and 8 or equal to 8")

# if number between 8 and 12, display "number is between 8 and 12

if 8 < number <= 12:
    print("Number  is between 8 and 12 or equal to 12")
#if number superior to 12, display superior to 12

if number > 12:
    print("Number is superior to 12")
    
#if number inferior to 0, display inferior to 0 (zero)
if number < 0:
    print("Number is inferior to 0")
