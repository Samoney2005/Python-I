# ============================================
# Problem 1: Build a Binary Tree I
# ============================================
# --- UMPIRE Steps ---
# Understand: Goal: Create a specific 7-node binary tree structure using the TreeNode class.
# Match: Direct construction of objects and linking them via left/right attributes.
# Plan: 1. Create leaf nodes (4, 5, 6, 7). 2. Create intermediate nodes (2, 3), linking their children. 3. Create root (1), linking its children.
# Review: Inspect the resulting structure to ensure correct val and pointer links.
# Evaluate: Time O(1). Space O(1).
# --------------------
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

node1 = TreeNode(10)
node2 = TreeNode(4)
node3 = TreeNode(6)

node1.left = node2
node1.right = node3

# ============================================
# Problem 2: 3-Node Sum I
# ============================================
# --- UMPIRE Steps ---
# Understand: Goal: Check if root.val == root.left.val + root.right.val. Tree is guaranteed to have exactly 3 nodes.
# Match: Simple direct arithmetic comparison.
# Plan: Access root.left.val and root.right.val and check against root.val.
# Review: Test cases (10, 4, 6) -> True; (5, 3, 1) -> False. Looks correct.
# Evaluate: Time **O(1)**. Space **O(1)**.
# --------------------
class TreeNode:
       def __init__(self, val, left=None, right=None):
             self.val = val
             self.left = left
             self.right = right

def check_tree(root):
    sum = root.left.val + root.right.val
    if sum == root.val:
       return True
    else:
       return False


node1 = TreeNode(5)
node2 = TreeNode(3)
node3 = TreeNode(1)
node1.left = node2
node1.right = node3
root = node1
print(check_tree(root))

# ============================================
# Problem 3: 3-Node Sum II
# ============================================
# --- UMPIRE Steps ---
# Understand: Goal: Check if root.val == sum of children's values. Tree has at most 3 nodes. Missing children count as 0.
# Match: Conditional arithmetic. Must handle None children safely.
# Plan: 1. Handle root=None. 2. Define left_val/right_val as node.val if node exists, else 0. 3. Perform comparison.
# Review: Handles 3-node, 2-node (L or R), 1-node, and 0-node cases correctly.
# Evaluate: Time **O(1)**. Space **O(1)**.
# --------------------
class TreeNode:
    def __init__(self, val, left=None, right=None):
       self.val = val
       self.left = left
       self.right = right
def check_tree(root):
    if  root.left.val != None and  root.right.val != None:
       sum = root.left.val + root.right.val
       if sum == root.val:
          return True
    elif root.left.val == root.val or root.right.val == root.val :
          return True
    return False
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(2)
print (check_tree(root))


# ============================================
# Problem 4: Find Leftmost Node I (Recursive)
# ============================================
# --- UMPIRE Steps ---
# Understand: Goal: Find the value of the node reached by traversing only left child pointers from the root.
# Match: Recursion (follow left link until base case).
# Plan: Base Case: root is None or root.left is None. Recursive Step: Call function on root.left.
# Review: Checks edge cases (None, single node, right-skewed, general). Correct.
# Evaluate: Time **O(H)**, where H is tree height. Space **O(H)** for recursion stack.
# --------------------


# ============================================
# Problem 5: Find Leftmost Node II (Iterative)
# ============================================
# --- UMPIRE Steps ---
# Understand: Goal: Same as P4, but implemented iteratively.
# Match: Iteration (use a while loop to repeatedly follow the left link).
# Plan: 1. Initialize 'current' to root. 2. Loop while current.left is not None. 3. Return current.val.
# Review: Simple, direct path tracing. Correct.
# Evaluate: Time **O(H)**, where H is tree height. Space **O(1)**.
# --------------------


# ============================================
# Problem 6: In-order Traversal
# ============================================
# --- UMPIRE Steps ---
# Understand: Goal: Return a list of node values using In-order traversal (Left -> Root -> Right).
# Match: Recursion (standard DFS pattern).
# Plan: Define a recursive helper. Base case: node is None. Recursive calls: left, append val, right.
# Review: Test cases show correct ascending order for BSTs, and general L-R-R for non-BSTs. Correct.
# Evaluate: Time **O(N)**. Space **O(H)** for recursion stack, O(N) for result list.
# --------------------


# ============================================
# Problem 7: Binary Tree Size
# ============================================
# --- UMPIRE Steps ---
# Understand: Goal: Count the total number of nodes in the tree.
# Match: Recursion (summing up results from subtrees).
# Plan: Base case: root is None (return 0). Recursive step: 1 + size(left) + size(right).
# Review: Correctly handles empty tree (0) and any non-empty tree.
# Evaluate: Time **O(N)**. Space **O(H)** for recursion stack.
# --------------------


# ============================================
# Problem 8: Binary Tree Find
# ============================================
# --- UMPIRE Steps ---
# Understand: Goal: Check if a given value exists in the tree. Tree is general (not BST).
# Match: DFS/BFS traversal (Recursion used here).
# Plan: Check current node. If not found, recursively check left OR right subtree. Stop as soon as found.
# Review: Checks all nodes in the worst case. Correct.
# Evaluate: Time **O(N)**. Space **O(H)** for recursion stack.
# --------------------


# ============================================
# Problem 9: Binary Search Tree Find
# ============================================
# --- UMPIRE Steps ---
# Understand: Goal: Check if a given value exists in a BST. Use the BST property for efficiency.
# Match: Iteration (guided search).
# Plan: Start at root. If value is less than current, go left. If greater, go right. If equal, return True. Stop when current is None.
# Review: Efficiency is key; comparison correctly guides the search. Correct.
# Evaluate: Time **O(log N)** for balanced BST. Space **O(1)**.
# --------------------


# ============================================
# Problem 10: BST Descending Leaves
# ============================================
# --- UMPIRE Steps ---
# Understand: Goal: Find all leaves in a BST and return their values in descending order.
# Match: Reverse In-order Traversal (Right -> Root -> Left) combined with a leaf check.
# Plan: 1. Use a recursive helper. 2. Traverse Right. 3. Check if current node is a leaf; if so, append its value. 4. Traverse Left.
# Review: Reverse in-order ensures descending order; the leaf check filters out non-leaves. Correct.
# Evaluate: Time **O(N)** (must visit all nodes). Space **O(H)** for recursion stack.
# --------------------
