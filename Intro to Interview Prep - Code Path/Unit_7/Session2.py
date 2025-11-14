###############################################################
# 🧩 Problem 1: Neatly Nested
###############################################################

# Understand the Problem:
# Given a string of parentheses, determine recursively whether it is "neatly nested".
# A valid nesting example: "()", "(())", "(()())".
# Invalid examples: "())(", "(()", ")(".
# The input only contains '(' and ')'.

# Match (Identify Common Approaches):
# - This is a recursion and string validation problem.
# - Similar to checking balanced parentheses using stacks, but recursion can replace the stack.
# - Each recursive call checks an outer pair and dives inward.

# Plan a Solution (Step-by-Step):
# 1. Base Case: If the string is empty → return True.
# 2. If the first char is '(' and the last is ')' → recurse on substring inside.
# 3. Otherwise, return False.
# 4. Each recursive call peels off an outer layer of parentheses.

# Review the Solution:
# - Handles all nesting levels correctly.
# - Simpler than stack-based solutions but less efficient for large inputs due to slicing.

# Evaluate:
# Time Complexity:  O(n) — each call slices the string.
# Space Complexity: O(n) — recursion depth proportional to string length.
# Pros: Simple, elegant recursive logic.
# Cons: String slicing creates extra space; iterative stack method is more efficient for large n.
###############################################################

from re import I

def is_nested(s):
    if not s:
        return True
    if s[0] == "(" and s[-1] == ")":
        string = s[1:-1] #((()))
        return is_nested(string)

    return False

s = "(())"
print(is_nested(s))
s = "(()"
print(is_nested(s))

###############################################################
# 💡 Problem 2: How Many 1s
###############################################################

# Understand the Problem:
# You’re given a sorted binary array of 0s and 1s.
# Count how many 1s exist — efficiently (in O(log n) time).

# Match (Identify Common Approaches):
# - Classic binary search adaptation.
# - Similar to “find first occurrence” or “search boundary” problems.

# Plan a Solution (Step-by-Step):
# 1. Perform binary search to find the first index where element == 1.
# 2. Once found, total 1s = total length - first_one_index.
# 3. If 1 is not found at all, return 0.
# 4. Do not use linear counting — must remain O(log n).

# Review the Solution:
# - Efficient and concise.
# - Relies on sorted order of binary array.
# - Works for any number of 0s followed by 1s.

# Evaluate:
# Time Complexity:  O(log n)
# Space Complexity: O(1)
# Pros: Optimal for large sorted lists.
# Cons: Only works on sorted arrays; not general for unsorted input.
###############################################################

def binary_search(lst, low, high, target=1):
    low = 0
    high = len(lst) - 1
    target = 1
    if low > high:
        return -1

    mid = (low + high) // 2

    if lst[mid] == target:
        if mid == 0 or lst[mid - 1] == 0:
            return mid
        else:
            return binary_search(lst, low, mid - 1, target)
    elif lst[mid] < target:
        return binary_search(lst, mid + 1, high, target)
    else:
        return binary_search(lst, low, mid - 1, target)


def count_ones(lst):
    first_index = binary_search(lst, 0, len(lst) - 1)
    if first_index == -1:
        return 0
    return len(lst) - first_index


lst = [0, 0, 0, 1, 1, 1, 1]
print(count_ones(lst))

###############################################################
# 🔍 Problem 3: Binary Search IV
###############################################################

# Understand the Problem:
# Implement recursive binary search to find the index of a target in a sorted list.

# Match (Identify Common Approaches):
# - Binary search algorithm (divide and conquer).
# - Usually implemented iteratively; here we use recursion.

# Plan a Solution (Step-by-Step):
# 1. Define left and right boundaries.
# 2. Compute mid = (left + right) // 2.
# 3. If nums[mid] == target → return mid.
# 4. If target < nums[mid] → search in left half.
# 5. Else → search in right half.
# 6. Base case: if left > right → return -1.

# Review the Solution:
# - Uses recursion cleanly with base and recursive cases.
# - Equivalent performance to iterative version.

# Evaluate:
# Time Complexity:  O(log n)
# Space Complexity: O(log n) due to recursion stack.
# Pros: Simple and readable recursive form.
# Cons: Slightly higher memory usage than iterative approach.
###############################################################

def binary_search(lst, target, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2

    if lst[mid] == target:
        return mid
    elif lst[mid] > target:
        return binary_search(lst, target, low, mid - 1)
    else:
        return binary_search(lst, target, mid + 1, high)

nums = [1, 3, 5, 7, 9, 11, 13, 15]
target = 11
print(binary_search(nums, target, 0, len(nums) - 1))

###############################################################
# 🔄 Problem 4: Count Rotations
###############################################################

# Understand the Problem:
# Given a rotated sorted array with unique elements,
# find how many times the array has been rotated.
# This equals the index of the smallest element.

# Match (Identify Common Approaches):
# - Modified binary search.
# - Similar to “find minimum in rotated sorted array”.

# Plan a Solution (Step-by-Step):
# 1. Set left and right pointers at array ends.
# 2. If array segment is already sorted → left index is answer.
# 3. Compute mid.
# 4. Compare nums[mid] with neighbors (or left/right bounds):
#    - If nums[mid] is smaller than both → rotation count = mid.
#    - If nums[mid] >= nums[left] → smallest lies to the right.
#    - Else → smallest lies to the left.
# 5. Continue until smallest found.

# Review the Solution:
# - Uses binary search efficiently.
# - Avoids full traversal; logarithmic search.

# Evaluate:
# Time Complexity:  O(log n)
# Space Complexity: O(1)
# Pros: Very efficient for large arrays.
# Cons: Requires array with distinct elements for correct logic.
###############################################################
def count_rotations(nums):
    for i in range(len(nums)):
        if nums[i + 1] < nums[i]:
            return i + 1

Input = [6, 8, 9, 10, 2, 5]

print(count_rotations(Input))
###############################################################
# ⚙️ Problem 5: Merge Sort I
###############################################################

# Understand the Problem:
# Sort an array using Merge Sort.
# Merge Sort splits the list into halves recursively, sorts each half, and merges.

# Match (Identify Common Approaches):
# - Divide and conquer sorting algorithm.
# - Similar structure to Quick Sort but stable and guaranteed O(n log n).

# Plan a Solution (Step-by-Step):
# 1. Base case: if the list has 0 or 1 elements → return it (already sorted).
# 2. Split list into left and right halves.
# 3. Recursively apply merge_sort() on both halves.
# 4. Use helper function merge(left, right) to combine into a sorted list.
# 5. Return merged result.

# Review the Solution:
# - Stable sorting algorithm.
# - Performs well even on large data sets.
# - Requires auxiliary space for merging.

# Evaluate:
# Time Complexity:  O(n log n)
# Space Complexity: O(n)
# Pros: Stable, predictable performance.
# Cons: Requires extra memory; not in-place.
###############################################################
# Helper function: Merges two sorted lists into one sorted list
def merge(left, right):
    result = []  # List to store the merged result
    i = j = 0  # Pointers to iterate over left and right input arrays

    # Compare elements from left and right halves of the list and add them to the
    # result list in the correct order
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # Add any remaining elements from the left half to the result list
    while i < len(left):
        result.append(left[i])
        i += 1

    # Add any remaining elements from the right half to the result list
    while j < len(right):
        result.append(right[j])
        j += 1

    return result


def merge_sort(lst):
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]

    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    return merge(left_sorted, right_sorted)


Input = [5, 3, 4, 2, 1]
print(merge_sort(Input))

###############################################################
# 🎯 Problem 6: Circle Search
###############################################################

# Understand the Problem:
# Given a rotated sorted list with unique elements,
# find the index of a target element.

# Match (Identify Common Approaches):
# - Modified binary search.
# - Common variant of searching in rotated sorted arrays.

# Plan a Solution (Step-by-Step):
# 1. Initialize left and right pointers.
# 2. While left <= right:
#    a. Compute mid.
#    b. If nums[mid] == target → return mid.
#    c. Determine which half is sorted:
#        - If left half sorted:
#            If target lies within it → search left.
#            Else → search right.
#        - Else (right half sorted):
#            If target lies within it → search right.
#            Else → search left.
# 3. If not found → return -1.

# Review the Solution:
# - Efficiently narrows down search space without fully scanning.
# - Works because one half is always sorted in rotated array.

# Evaluate:
# Time Complexity:  O(log n)
# Space Complexity: O(1)
# Pros: Fast and optimal for sorted-rotated data.
# Cons: Slightly more complex than regular binary search logic.
###############################################################
