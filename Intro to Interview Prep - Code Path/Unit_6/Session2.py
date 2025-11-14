# ============================================
# Problem 1: Detect Circular Linked List
# ============================================
# Understand:
# We are given the head of a linked list.
# A circular linked list specifically connects the last node to the first node (head).
# We must return True if the list is circular, False otherwise.

# Plan (Pseudocode):
# 1. If head is None → return False
# 2. Set current = head.next
# 3. While current is not None and current is not head:
#       current = current.next
# 4. If current == head → return True
#    Else → return False

# Evaluate:
# Time Complexity: O(n) – Each node visited once.
# Space Complexity: O(1) – Constant number of pointers used.
# Variables:
#   head: starting node
#   current: node pointer used for traversal
# Rationale: Single traversal with no extra storage.
def is_circular(head):
 current = head.next
 while current:
  if current == head:
   return True
  current = current.next
 return False

# num1 -> num2 -> num3 -> num1
num1 = Node(1)
num2 = Node(2)
num3 = Node(3)
num4 = Node(4)
num1.next = num2
num2.next = num3
num3.next = num4
num4.next = num1
print(is_circular(num1))

# var1 -> var2 -> var3
var1 = Node(1)
var2 = Node(2)
var3 = Node(3)
var1.next = var2
var2.next = var3
print(is_circular(var1))
print()

# ============================================
# Problem 2: Find Last Node in a Linked List Cycle
# ============================================
# Understand:
# We must find the last node that connects back to the start of a cycle.
# If no cycle exists, return None.

# Plan (Pseudocode):
# 1. Use Floyd’s Cycle Detection:
#       slow = head
#       fast = head
# 2. Move slow by 1 step, fast by 2 steps until they meet or fast reaches None.
# 3. If no meeting point → return None (no cycle)
# 4. Move slow to head. Move both pointers 1 step at a time to find cycle start.
# 5. Once start found, traverse from that node until next == start.
# 6. Return that node (the last node in the cycle).

# Evaluate:
# Time Complexity: O(n) – Two passes at most.
# Space Complexity: O(1) – Only uses pointers.
# Variables:
#   slow, fast: detection pointers
#   start: first node of cycle
# Rationale: Uses Floyd’s algorithm for cycle detection efficiently.

def find_last_node_in_cycle(head):
    slow, fast = head, head
    # step 1 detecting the cycle (IF THE CYCLE EXISTS)
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        # if they ever meet: CYCLE EXISTS
        if slow == fast:
            break

    # IF THEY NEVER MEET
    if slow != fast:
        return None

    # part 2: finding the starting node of the cycle
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    # part 3: finding the last node in the cycle
    cycle_start = slow
    while fast != cycle_start:
        fast = fast.next
    return fast


num1 = Node(1)
num2 = Node(2)
num3 = Node(3)
num4 = Node(4)
num2 = num1.next
num2 = num3.next
num3 = num4.next
num4 = num1.next
print(find_last_node_in_cycle(num1).value)








# ============================================
# Problem 3: Partition List Around Value
# ============================================
# Understand:
# Given a linked list and a value val,
# rearrange nodes so that nodes < val come before nodes >= val.
# Maintain the original relative order within each group.

# Plan (Pseudocode):
# 1. Create two dummy heads:
#       before_head, after_head
# 2. Initialize tails:
#       before = before_head
#       after = after_head
# 3. Traverse the list:
#       if current.value < val:
#           before.next = current
#           before = before.next
#       else:
#           after.next = current
#           after = after.next
#       current = current.next
# 4. Join two lists:
#       before.next = after_head.next
#       after.next = None
# 5. Return before_head.next

# Evaluate:
# Time Complexity: O(n) – Single traversal of list.
# Space Complexity: O(1) – Reuses existing nodes.
# Variables:
#   before_head, after_head: temporary dummy nodes
#   before, after: pointers for building partitions
# Rationale: Uses two-list technique to organize nodes efficiently.

# ============================================
# Problem 4: Convert Binary Number in a Linked List to Integer
# ============================================
# Understand:
# Each node contains 0 or 1.
# The linked list represents a binary number with the most significant bit at the head.

# Plan (Pseudocode):
# 1. Initialize num = 0
# 2. Traverse list:
#       num = num * 2 + current.value
#       current = current.next
# 3. Return num

# Evaluate:
# Time Complexity: O(n) – Process each node once.
# Space Complexity: O(1) – Only integer accumulator used.
# Variables:
#   num: integer value of binary
# Rationale: Binary to decimal conversion in one pass.

# ============================================
# Problem 5: Add Two Numbers Represented by Linked Lists
# ============================================
# Understand:
# Each linked list represents a number in reverse order.
# Each node holds one digit.
# We add them and return a linked list of the sum in reverse order.

# Plan (Pseudocode):
# 1. Initialize:
#       carry = 0
#       dummy_head = Node(0)
#       current = dummy_head
# 2. While head_a, head_b, or carry exist:
#       val1 = head_a.value if head_a else 0
#       val2 = head_b.value if head_b else 0
#       total = val1 + val2 + carry
#       carry = total // 10
#       new_digit = total % 10
#       current.next = Node(new_digit)
#       current = current.next
#       move head_a and head_b forward if not None
# 3. Return dummy_head.next

# Evaluate:
# Time Complexity: O(max(m, n)) – Traverse both lists once.
# Space Complexity: O(max(m, n)) – Output list proportional to sum length.
# Variables:
#   carry: integer carryover between digits
#   current: pointer to build new list
# Rationale: Simulates manual addition digit by digit.

# ============================================
# Problem 6: Reverse Sublist of a Linked List
# ============================================
# Understand:
# We must reverse a section of the list between indices m and n (1-based).
# Return the modified list.

# Plan (Pseudocode):
# 1. If m == n → return head (nothing to reverse)
# 2. Create dummy = Node(0, head)
# 3. Move pre pointer to node before position m
# 4. Start reversing from m to n using:
#       prev = None
#       current = pre.next
#       Repeat (n - m + 1) times:
#           temp = current.next
#           current.next = prev
#           prev = current
#           current = temp
# 5. Connect sublist:
#       pre.next.next = current
#       pre.next = prev
# 6. Return dummy.next

# Evaluate:
# Time Complexity: O(n) – Single pass through list.
# Space Complexity: O(1) – Reversal done in place.
# Variables:
#   pre: node before sublist
#   prev, current: used for in-place reversal
# Rationale: Efficient in-place sublist reversal.
