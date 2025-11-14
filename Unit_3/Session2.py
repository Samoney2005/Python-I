# Problem 1: Sum of Strings
def sum_of_number_strings(nums):
    total = 0
    for str in nums:
        total += int(str)
    return total
nums = ["10", "20", "30"]
sum = sum_of_number_strings(nums)
print(sum)
    
# Problem 2: Remove Duplicates
def remove_duplicates(nums):
    new_list = []
    for i in nums:
      if i not in new_list:
          new_list.append(i) 
    return new_list
nums = [1,1,1,2,3,4,4,5,6,6]
print(remove_duplicates(nums))


# Understand
# we have a list duplicate numbers, we must remove the duplicates 

# Plan 
# intialize a new list, for i in nums , (go through each one),modify the original list, return the new list


# Implement

# Problem 3: Reverse Letters
def reverse_only_letters(s):
s = "a-bC-dEf-ghIj"
reversed_s = reverse_only_letters(s)
print(reversed_s)

# Problem 4: Longest Uniform Substring


# Problem 5: Teemo's Attack

# Problem 6: Sum Unique Elements


