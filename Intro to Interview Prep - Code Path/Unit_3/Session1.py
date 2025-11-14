# Problem 1: Calling Mississippi
def count_mississippi(limit):
    for num in range(1, limit):
        print( f"{num} mississippi")
count_mississippi(6)

# Problem 2: Swap Ends
def swap_ends(my_str):
    if len(my_str) < 2:
        return my_str
    return my_str[-1] + my_str[1:-1] + my_str[0]
print(swap_ends("boat"))

# Problem 3: Is Pangram

#U
# input case with english alphabet
# s.lower needed 

#P
# if my_str = pangram output- (True)
# else output (False)

def is_pangram(my_str):
    my_str = my_str.lower()
    alpha = "abcdefghijklmnopqrstuvwxyz"
    for x in alpha:
        if x not in my_str:
            return False
    return True
my_str = "The quick brown fox jumps over the lazy dog"
print(is_pangram(my_str))

str2 = "The dog jumped"
print(is_pangram(str2))
