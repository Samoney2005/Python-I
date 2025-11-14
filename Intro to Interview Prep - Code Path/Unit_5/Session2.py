# ============================================
# Problem 1: Battle Pokemon
# ============================================
# Understand:
# We need to define an 'attack()' method inside the Pokemon class
# that decreases the opponent's HP based on the attacker's damage.
# It should also print the result depending on whether the opponent fainted.
#
# Plan:
# 1. Define the attack() method taking 'self' and 'opponent'.
# 2. Subtract self.damage from opponent.hp.
# 3. If opponent.hp <= 0:
#       - Set opponent.hp = 0
#       - Print "<Opponent name> fainted"
#    Else:
#       - Print "<Pokemon name> dealt <damage> damage to <opponent name>"
# 4. No value needs to be returned.
#
# Implement:

class Pokemon():
	def  __init__(self, name, hp, damage):
		self.name = name
		self.hp = hp # hit points
		self.damage = damage # The amount of damage this pokemon does to its opponent every attack
		
	def attack(self, opponent):
		pass

# ============================================
# Problem 2: Convert to Linked List
# ============================================
# Understand:
# We must recreate the list ["Jigglypuff", "Wigglytuff"] as a linked list.
# Each Node points to the next one, and the final node points to None.
#
# Plan:
# 1. Create a Node class with 'value' and 'next' attributes.
# 2. Create two nodes: node_1 ("Jigglypuff") and node_2 ("Wigglytuff").
# 3. Link node_1.next = node_2.
# 4. node_2.next should remain None (end of list).
# 5. Verify with prints to confirm linking order.
#
# Implement:

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next


# ============================================
# Problem 3: Add First
# ============================================
# Understand:
# We need to insert a new node at the beginning of a linked list
# and make that new node the new head.
#
# Plan:
# 1. Define add_first(head, new_node).
# 2. Set new_node.next = head.
# 3. Return new_node as the new head.
# 4. The original list should now follow the new node.
#
# Implement:

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
		
		
def add_first(head, new_node):
	pass

# ============================================
# Problem 4: Get Tail
# ============================================
# Understand:
# We must return the value of the last node (the tail) in a linked list.
# If the list is empty, return None.
#
# Plan:
# 1. Define get_tail(head).
# 2. If head is None → return None.
# 3. Traverse using a while loop until current.next is None.
# 4. Return current.value when the loop ends.
#
# Implement:

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

def get_tail(head):
	pass

# ============================================
# Problem 5: Replace Node
# ============================================
# Understand:
# We need to replace every node value equal to 'original' with 'replacement'.
# The modification happens directly in the existing linked list.
#
# Plan:
# 1. Define ll_replace(head, original, replacement).
# 2. Start from head and traverse while current is not None.
# 3. If current.value == original → set current.value = replacement.
# 4. Continue until the end.
# 5. Return None (list updated in place).
#
# Implement:
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
		
def ll_replace(head, original, replacement):
	pass

 
def to_string(head): # to test your list
    parts, cur = [], head
    while cur:
        parts.append(str(cur.value))
        cur = cur.next
    return " -> ".join(parts) if parts else "EMPTY"

# ============================================
# Problem 6: List Nodes
# ============================================
# Understand:
# We need a function that collects the values of the first 'n' nodes
# from a linked list and returns them as a Python list.
#
# Plan:
# 1. Define listify_first_n(head, n).
# 2. Create an empty Python list 'values'.
# 3. Traverse through the linked list, adding node values to 'values'.
# 4. Stop after 'n' nodes or if the list ends early.
# 5. Return 'values'.
#
# Implement:
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

def listify_first_n(head, n):
	pass

# ============================================
# Problem 7: Insert Value
# ============================================
# Understand:
# We must insert a new Node with value 'val' at a given index 'i' in a linked list.
# If index exceeds list length, append to the end.
#
# Plan:
# 1. Define ll_insert(head, val, i).
# 2. If i == 0 → create new node and insert at head.
# 3. Else:
#       - Traverse until the (i-1)-th node or end of list.
#       - Insert new Node between current and current.next.
# 4. If list ends before reaching i → append to end.
# 5. Return head.
#
# Implement:
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
		
def ll_insert(head, val, i):
	pass

# ============================================
# Problem 8: Linked Listify
# ============================================
# Understand:
# We must convert a normal Python list into a linked list.
# Each element becomes a Node connected to the next.
#
# Plan:
# 1. Define list_to_linked_list(lst).
# 2. If lst is empty → return None.
# 3. Create head Node from the first element.
# 4. Loop through remaining items, creating and linking new nodes.
# 5. Return head of the linked list.
#
# Implement:
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def list_to_linked_list(lst):
    pass

# ============================================
# Problem 9: Doubly Linked List
# ============================================
# Understand:
# We must recreate ["Poliwag", "Poliwhirl", "Poliwrath"] as a doubly linked list.
# Each node should point forward and backward.
#
# Plan:
# 1. Define a Node with value, next, and prev.
# 2. Create three nodes for Poliwag, Poliwhirl, and Poliwrath.
# 3. Link forward: poliwag.next = poliwhirl, poliwhirl.next = poliwrath.
# 4. Link backward: poliwhirl.prev = poliwag, poliwrath.prev = poliwhirl.
# 5. Verify by printing middle node’s prev and next values.
#
# Implement:
class Node:
	def __init__(self, value, next = None, prev = None):
		self.value = value
		self.next = next
		self.prev = prev

# ============================================
# Problem 10: Print Backwards
# ============================================
# Understand:
# We need to print the values of a doubly linked list in reverse order
# starting from the tail, separated by spaces.
#
# Plan:
# 1. Define print_reverse(tail).
# 2. While current node is not None:
#       - Print current.value followed by a space.
#       - Move to current.prev.
# 3. Stop when there are no previous nodes left.
# 4. Ensure correct reverse order in output.
#
# Implement:
class Node:
	def __init__(self, value, next = None, prev = None):
		self.value = value
		self.next = next
		self.prev = prev
		
def print_reverse(tail):
	pass
