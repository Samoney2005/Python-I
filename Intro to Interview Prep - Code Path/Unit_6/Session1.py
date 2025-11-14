# ============================================
# Problem 1: Nested Constructors
# ============================================
# Understand:
# We need to create a linked list 4 -> 3 -> 2 using a single line of code
# with nested constructor calls to the Node class.
# Each Node should contain a value and a reference to the next node.
#
# Plan:
# 1. Use the Node class that has __init__(self, value, next=None).
# 2. Create the linked list in one statement using nested constructors:
#       Node(4, Node(3, Node(2)))
# 3. This results in:
#       head = 4 -> 3 -> 2
# 4. Print or traverse to confirm the order.
#
# Implement:

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
# Creating the linked list 4 -> 3 -> 2
head = Node(4, Node(3, Node(2)))
# Function to print the linked list for verification
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next  
print_linked_list(head)





# ============================================
# Problem 2: Find Frequency
# ============================================
# Understand:
# We must count how many times a given value 'val' appears in a linked list.
# We’ll traverse the list from head to tail, comparing each node’s value.
#
# Plan:
# 1. Define count_element(head, val).
# 2. Initialize a counter variable = 0.
# 3. Traverse through the list using a while loop.
# 4. If current.value == val → increment counter.
# 5. Continue until reaching the end (current becomes None).
# 6. Return counter.
#
# Time Complexity: O(n)
# - We visit each node once.
# Space Complexity: O(1)
# - Only a few variables are used regardless of list size.
#
# Implement:

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
# Put the head here 
head = Node(3, Node(1, Node(2, Node(1))))
# Define count_element
def count_element(head, val):
    count = 0
    current = head
    while current:
        if current.value == val:
            count += 1
        current = current.next
    return count
print(count_element(head, 1)) 


# ============================================
# Problem 3: Remove Tail
# ============================================
# Understand:
# The provided remove_tail() function tries to remove the last node
# but contains a bug. We must find and fix it so it removes the tail correctly.
#
# Plan:
# 1. Test the code with lists like 1 -> 2 -> 3 -> 4.
# 2. Observe output or stack trace.
# 3. Identify that the while loop goes one node too far:
#       current = current.next continues until current is the last node,
#       not the second-to-last.
# 4. Fix: loop should stop when current.next.next is None.
# 5. Then set current.next = None.
# 6. Return the head.
#
# Example:
# Input: 1 -> 2 -> 3 -> 4
# Output: 1 -> 2 -> 3
#
# Implement:

class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next      
# Helper function to print the linked list
def print_list(node):
    current = node
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()

# I have a bug! 
def remove_tail(head):
    if head is None: # If the list is empty, return None
        return None
    if head.next is None: # If there's only one node, removing it leaves the list empty
        return None 
		
	# Start from the head and find the second-to-last node
    current = head
    while current.next.next: 
        current = current.next

    current.next = None # Remove the last node by setting second-to-last node to None
    return head

head = Node(1, Node(2, Node(3, Node(4))))
head = remove_tail(head)

current = head
while current:
    print( current.value, end=" -> " if current.next else "")
    current = current.next


# ============================================
# Problem 4: Find the Middle
# ============================================
# Understand:
# We must use the slow-fast pointer technique to find the middle of a linked list.
# If there are two middle nodes, return the second one.
#
# Plan:
# 1. Define find_middle_element(head).
# 2. Initialize two pointers: slow = head, fast = head.
# 3. Move slow by one step, fast by two steps each loop.
# 4. When fast reaches the end (fast is None or fast.next is None),
#    slow will be at the middle.
# 5. Return slow.value.
#
# Time Complexity: O(n)
# - Each node is visited once by fast/slow pointers.
# Space Complexity: O(1)
# - Only two pointers used.
#
# Implement:

class Node:
   def __init__(self, value, next=None):
       self.value = value
       self.next = next

def find_middle_element(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next          # Move slow pointer by one
        fast = fast.next.next     # Move fast pointer by two
    return slow.value
    if slow == fast:          # If they meet, there's a cycle
            return True
    return False  # If fast reaches the end, no cycle
head = Node(1, Node(2, Node(3)))
print(find_middle_element(head))

# ============================================
# Problem 5: Is Palindrome?
# ============================================
# Understand:
# We must determine if a linked list reads the same forwards and backwards.
# Use two-pointer or reverse-half techniques to check for symmetry.
#
# Plan:
# 1. Define is_palindrome(head).
# 2. Use slow and fast pointers to find the middle.
# 3. Reverse the second half of the list in place.
# 4. Compare the first half and the reversed second half node by node.
# 5. If all match → return True, else False.
#
# Time Complexity: O(n)
# - Each node is visited a few times (find middle + reverse + compare).
# Space Complexity: O(1)
# - Reversal done in place, no extra list storage.
#
# Implement:


# ============================================
# Problem 6: Put it in Reverse
# ============================================
# Understand:
# We need to reverse the entire linked list in place and return the new head.
# No new list should be created.
#
# Plan:
# 1. Define reverse(head).
# 2. Initialize three pointers: prev = None, current = head, next_node = None.
# 3. Traverse while current:
#       - Save current.next in next_node.
#       - Set current.next = prev.
#       - Move prev = current, current = next_node.
# 4. When finished, prev will be the new head.
# 5. Return prev.
#
# Time Complexity: O(n)
# - Each node is visited once.
# Space Complexity: O(1)
# - Only a few pointers used.
#
# Example:
# Input: 1 -> 2 -> 3 -> 4
# Output: 4 -> 3 -> 2 -> 1
#
# Implement: