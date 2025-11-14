## Problem 1: Print "hello world!" to the console
def hello_world():
    print("hello world!")
hello_world()

## Problem 2: Change the emoji to reflect your mood today
def todays_mood():
    mood = input("What's is your mood today?: ")
    print("Today's mood: " + mood)
todays_mood()

## Problem 3: Create a function that prints out today's lunch menu
def print_menu():
    menu = input("What's for lunch today?: ")
    print("Lunch today is: " + menu)
print_menu()

## Problem 4: Create a function that takes two numbers as input and returns their sum
def print_sum():
    sum_one = int(input("Enter first number: ")) 
    sum_two = int(input("Enter second number: "))
    total_sum = sum_one + sum_two
    return str(total_sum)
sum = print_sum()
print("The sum is: " + sum)

## Problem 4.1: Ask the user if they want to double their sum
double_sum = (input("Can we double your sum?"))
if double_sum == "yes":
    print("Your double sum is: " + str(int(sum) * 2))
elif double_sum == "no":
    print("Okay, your sum remains: " + sum)



## Problem 5: Create a function that takes two numbers as input and returns their sum
def print_product():
    product_one = int(input("Enter first number: ")) 
    product_two = int(input("Enter second number: "))
    total_product = product_one * product_two
    return str(total_product)
product = print_product()
print("The product is: " + product)

## Problem 6: Create a function that classifies a person based on their age
def classify_age():
    age = int(input("Enter your age: "))
    if age < 18:
        output = "You are a child!"
        print(output)
    if age >= 65:
        output = " You are a senior!"
        print(output)
    else:
        output = "You are an adult!"
        print(output)
age = classify_age()

## Problem 7: What time is it?
def what_time_is_it():
    hour = int(input("What time is it?"))
    if hour == 12:
        output = "peanut butter jelly time 🥪"
        print(output)
    elif hour == 2:
        output = "taco time 🌮"
        print(output)
    else:
        output = "It's nap time 😪"
    print(output)
hour = what_time_is_it()

## Problem 8: Blackjack
def blackjack():
    name = (input("Enter your name:"))
    score = int(input("Enter your score:"))
    if score == 21:
        output = "BlackJack!"
        print(output)
    elif score > 21:
        output = "Bust!"
    elif score >= 17 and score < 21:
        output = "Nice Hand!"
        print(output)
    else:
        output = "Hit me!"
        print(output)
score = blackjack()

## Problem 9: Last Item
lst = [3,1,6,7,5]
def get_first(lst):
    print("The first item is", lst[:1])
get_first(lst)

## Problem 10: Last Item
lst = [3,1,6,7,5]
def get_last(lst):
    print("The last item is", [5])
get_last(lst)

## Problem 11: Counter
def counter(stop):
    count = 0 
    for i in range (1,7):
        print(i)
counter(7)

## Problem 12: Sum of 1 to 10
def sum_ten(stop):
    sum = 0           
    for i in range(1, stop+1):   
        sum = sum + i   
        print(sum)
sum_ten(10)


## Problem 13: Total Sum
def sum_positive_range(stop):
    total = 0
    for i in range(1, stop+1):
        total = total + i
    print("This is the total:",total)   
sum_positive_range(6) 

## Problem 14: Total Sum in Range

def sum_range(start, stop):
    total = 0
    for i in range(3, stop+1):
        total = total + i
    print("The total is:", total)
sum_range(3,9)

## Problem 15: Negative Numbers
'''
 Write a function 
print_negatives() that takes a list of integers 
lst and prints all negative
 numbers in the list.

def print_negatives(lst):
 Example Usage: print_negatives([3,-2,2,1,-5])
 Example Output:-2-5
 Example Usage: print_negatives([1,2,3,4,5])
 Example Output:
 None
'''
def print_negatives(lst):
    print_negatives([3,-2,2,1,-5])
    











    


    

        

    


