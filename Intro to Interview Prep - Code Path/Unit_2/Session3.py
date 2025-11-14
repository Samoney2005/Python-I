# Problem 1: All In
lst_1 = [1,2]
lst_2 = [1,2,3]
def all_in(a,b):
    if a == b:
        output = "True"
        print(output)
    else:
        output = "False"
        print(output)
all_in(lst_1,lst_2)

# Problem 2: Create a Dictionary
def create_dictionary(keys, values):
    hashmap = {}
    for i in range(0, len(keys)):
            hashmap[keys[i]] = values[i]

    return hashmap
keys = ['peanut', 'dragon', 'star', 'pop', 'space']
values = ['butter', 'fly', 'fish', 'corn', 'ship']
print(create_dictionary(keys, values))

# Problem 3: Print Pair



# Problem 4: Keys Versus Values

# Problem 5: Restock Inventory

# Problem 6: Calculate GPA

# Problem 7: Best Book

# Problem 8: Index-Value Map
