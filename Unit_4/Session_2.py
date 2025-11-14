# Problem 1: Prime Number
def is_prime(n):
    if n == 1:
        return False
    for i in range(1,n):
        if n % i == 0 and i != 1 and i != n:
            return False
    return True
print(is_prime(5))
print(is_prime(12))
print(is_prime(9))

# Understand: If number is prime = True otherwise False.
# Plan: Use a While loop, while n mod, use a counter, for the case that
# its not true check if its equal to n and if not then its false.

# Problem 2: Two-Pointer Reverse List
def reverse_list(lst):
    leftPointer = 0
    rightPointer = len(lst) - 1
    while leftPointer < rightPointer:
        tempVar = lst[leftPointer]
        lst[leftPointer] = lst[rightPointer]
        lst[rightPointer] = tempVar
        leftPointer += 1
        rightPointer -= 1