# ============================================
# Problem 1: Hello Hello
# ============================================
# --- UMPIRE Steps (Comparison) ---
# Understand: Goal: Print "Hello" 'n' times using recursion and iteration.
# Match: Recursive and Iterative patterns.
# Plan (Iterative): Use a for loop to iterate n times and print "Hello".
# Review: Both solutions successfully print the output n times.
# Evaluate: Time O(n) for both. Space O(n) for recursive, O(1) for iterative.
# ------------------------------------
def repeat_hello(n):
    if n > 0:
        print("Hello")
        repeat_hello(n - 1)


# Example Usage:
# print("--- Recursive Output ---")
# repeat_hello(5)

def repeat_hello_iterative(n):
    # IMPLEMENTATION START
    for i in range(n):
        print("Hello")


# IMPLEMENTATION END

# Example Usage:
# print("\n--- Iterative Output ---")
# repeat_hello_iterative(5)


# ============================================
# Problem 2: Factorial Cases
# ============================================

# --- UMPIRE Steps ---
# Understand: Calculate n! recursively (n! = n * (n-1)!). Base Case: 0! = 1.
# Match: Classic recursive pattern (Direct Recursion).
# Plan: If n=0, return 1. Else, return n * factorial(n - 1).
# Review: Tracing factorial(3) gives 3 * 2 * 1 * 1 = 6. Correct.
# Evaluate: Time O(n). Space O(n) (call stack depth).
# ------------------------------------
def factorial(n):
    # IMPLEMENTATION START
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    # IMPLEMENTATION END


# Example Usage:
# print("\n--- Problem 2 Output ---")
# print(f"factorial(5) = {factorial(5)}") # Expected Output: 120

# ============================================
# Problem 3: Recursive Sum
# ============================================

# --- UMPIRE Steps ---
# Understand: Sum list elements recursively without using sum().
# Match: Classic recursive list traversal.
# Plan: Base Case: empty list returns 0. Recursive Case: lst[0] + sum_list(lst[1:]).
# Review: Tracing sum_list([1, 2]) gives 1 + (2 + 0) = 3. Correct.
# Evaluate: Time O(n). Space O(n) (call stack depth).
# ------------------------------------
def sum_list(lst):
    # IMPLEMENTATION START
    if not lst:
        return 0
    return lst[0] + sum_list(lst[1:])
    # IMPLEMENTATION END

# Example Usage:
# print("\n--- Problem 3 Output ---")
# print(f"sum_list([1, 2, 3, 4, 5]) = {sum_list([1, 2, 3, 4, 5])}") # Expected Output: 15

# Part 1 : Instructor Lead Session
# 🧑‍💻 Part 2: Breakout Session

# ============================================
# Problem 4: Recursive Power of 2
# ============================================

# --- UMPIRE Steps ---
# Understand:
#   - Goal: Determine if a positive integer 'n' is a power of two ($n = 2^x$).
#   - Constraint: Must be solved **recursively**.
#
# Match: Recursive division pattern. Since $2^x / 2 = 2^{x-1}$, repeatedly dividing a power of two by 2 will eventually yield 1.
#
# Plan:
# 1. Define `is_power_of_two(n)`.
# 2. **Initial/Failure Check**: If $n \le 0$, return `False`.
# 3. **Base Case**: If $n == 1$, return `True` ($2^0 = 1$).
# 4. **Failure Check**: If $n$ is odd ($n \% 2 \ne 0$) and not 1, return `False`.
# 5. **Recursive Case**: Else, check the result of calling `is_power_of_two(n / 2)`.
#
# Review:
#   - Tracing $n=16$: $16 \rightarrow 8 \rightarrow 4 \rightarrow 2 \rightarrow 1 \rightarrow True$.
#   - Tracing $n=18$: $18 \rightarrow 9$. $9 \% 2 \ne 0$, returns `False`. Correct.
#
# Evaluate:
#   - Time Complexity: $\mathbf{O(\log n)}$ - The input is halved in each step.
#   - Space Complexity: $\mathbf{O(\log n)}$ - The depth of the recursive call stack is proportional to $\log_2 n$.
# ------------------------------------
def is_power_of_two(n):
	pass
# Example Usage:
# print(is_power_of_two(16)) # True
# print(is_power_of_two(18)) # False


# ============================================
# Problem 5: Binary Search I (Iterative)
# ============================================

# --- UMPIRE Steps ---
# Understand:
#   - Goal: Find the index of `target` in a **sorted** list `lst`.
#   - Constraint: Implement the **iterative** (non-recursive) Binary Search.
#
# Match: Standard Iterative Search (Divide and Conquer).
#
# Plan:
# 1. Define `binary_search(lst, target)`.
# 2. Initialize pointers: `left = 0`, `right = len(lst) - 1`.
# 3. Loop while `left <= right`.
# 4. Calculate `mid = (left + right) // 2`.
# 5. Compare `lst[mid]` to `target`:
#    - Match: return `mid`.
#    - `lst[mid] < target`: Search right half: `left = mid + 1`.
#    - `lst[mid] > target`: Search left half: `right = mid - 1`.
# 6. If loop finishes, return -1.
#
# Review:
#   - Tracing $target=11$: Search space is halved until $11$ at index $5$ is found. Correct.
#
# Evaluate:
#   - Time Complexity: $\mathbf{O(\log n)}$ - Search space is halved in each iteration.
#   - Space Complexity: $\mathbf{O(1)}$ - Constant extra space for pointers (`left`, `right`, `mid`).
# ------------------------------------
def binary_search(lst, target):
	pass
# Example Usage:
# lst = [1, 3, 5, 7, 9, 11, 13, 15], target = 11
# print(binary_search(lst, target)) # Expected Output: 5


# ============================================
# Problem 6: Backwards Binary Search (Find Last)
# ============================================

# --- UMPIRE Steps ---
# Understand:
#   - Goal: Find the index of the **last** occurrence of `target` in a sorted list (which may contain duplicates).
#
# Match: Variation of Iterative Binary Search. The key difference is how the search space is adjusted upon finding a match.
#
# Plan:
# 1. Define `find_last(lst, target)`.
# 2. Initialize pointers: `left`, `right`. Initialize `last_index = -1`.
# 3. Loop while `left <= right`.
# 4. Calculate `mid`.
# 5. If `lst[mid] == target`:
#    - Store `mid` in `last_index`.
#    - **Crucial Step**: Shift the search to the **right** (`left = mid + 1`) to find a potential later occurrence.
# 6. If `lst[mid] < target`: Search right half (`left = mid + 1`).
# 7. If `lst[mid] > target`: Search left half (`right = mid - 1`).
# 8. Return `last_index`.
#
# Review:
#   - If $target=11$ is found at index $5$, the search continues on the indices $>5$ to ensure that if $11$ appears at index $6$, it is found and replaces the stored index. Correct.
#
# Evaluate:
#   - Time Complexity: $\mathbf{O(\log n)}$ - The search space is halved logarithmically.
#   - Space Complexity: $\mathbf{O(1)}$ - Constant extra space.
# ------------------------------------
def find_last(lst, target):
	pass
# Example Usage:
# lst = [1, 3, 5, 7, 9, 11, 11, 13, 15], target = 11
# print(find_last(lst, target)) # Expected Output: 6


# ============================================
# Problem 7: Find Floor
# ============================================

# --- UMPIRE Steps ---
# Understand:
#   - Goal: Find the index of the **floor** of a value $x$.
#   - Definition: The largest element in the sorted list that is $\le x$. Return -1 if no element is $\le x$.
#
# Match: Variation of Iterative Binary Search, aiming to converge on the closest value from below.
#
# Plan:
# 1. Define `find_floor(lst, x)`.
# 2. Initialize pointers: `left`, `right`. Initialize `floor_index = -1`.
# 3. Loop while `left <= right`.
# 4. Calculate `mid`.
# 5. If `lst[mid] == x`: Return `mid` (the exact floor).
# 6. If `lst[mid] < x`:
#    - This is a potential floor. Store `mid` in `floor_index`.
#    - Shift search to the **right** (`left = mid + 1`) to search for a *larger* element that might *still* be $\le x$.
# 7. If `lst[mid] > x`: This value is too large. Search left half (`right = mid - 1`).
# 8. Return `floor_index`.
#
# Review:
#   - Tracing $x=5$ in $[1, 2, 8, 10]$: When $2$ is found, its index is saved, and the search continues right (for $8, 10$). Since $8$ is too large, the search space shrinks, but the saved index of $2$ is preserved. Correct.
#
# Evaluate:
#   - Time Complexity: $\mathbf{O(\log n)}$ - The search space is divided logarithmically.
#   - Space Complexity: $\mathbf{O(1)}$ - Constant extra space.
# ------------------------------------
def find_floor(lst, x):
	pass
# Example Usage:
# lst = [1, 2, 8, 10, 11, 12, 19], x = 5
# print(find_floor(lst, x)) # Expected Output: 1 (Index of 2)