## Problem 1: Printed List 
lst = ["squirtle", "gengar", "charizard", "pikachu"]
def print_list(lst):
    for item in lst:
        print(item)
print_list(lst)


## Problem 2: Print Doubled List Items
lst = [1,2,3]

def doubled(lst):
  for num in lst:
    num = num * 2
    print(num)

doubled(lst)

## Problem 3: Return Doubled List

def doubled(lst):
    new_lst = []
    for num in lst:
        num = num * 2
        new_lst.append(num)
    return new_lst

## Problem 4: Flip Signs
lst = [1,-2,-3, 4]

def flip_sign(lst):
    new_lst = []
    for num in lst:
        num = num * -1
        new_lst.append(num)
    print(flip_sign(lst))


## Problem 5: Max Difference
lst = [5,22,8,10,2]
def max_difference(lst):
    least = lst[0] # least = 0  
    largest = lst[0]
    for num in lst:
        if num < least: # 5 < 0 False
            least = num
        if num > largest: # 5 < 0 True
            largest = num # largest = 5
    difference = largest - least
    print(difference)
max_difference(lst)

## Problem 6: Below Threshold
numbers = [12,8,2,4,4,10]
def count_less_than(numbers, threshold):
    count = 0
    for num in numbers:
        if num < threshold:
            count = count + 1
    print(count)
    count_less_than(numbers, 5)


## Problem 7: Evens List



## Problem 8: Multiples of Five


## Problem 9: Divisors


## Problem 10: FizzBuzz


## Problem 11: Print the Index

## Problem 12: Linear Search


## Problem 13: Convert Temperature




## Problem 14: Average Score

## Problem 15: Increment by 1


## Problem 16: Check for Number




 
