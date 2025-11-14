# ============================================
# Problem 1: Is Uni-valued
# ============================================
# --- UMPIRE Steps ---
# Understand: Check if every node in the tree has the same value. An empty tree is True.
# Match: Tree Traversal (DFS/Recursion).
# Plan:
# 1. If root is None, return True.
# 2. Check if left child exists and matches root value. If not, return False.
# 3. Check if right child exists and matches root value. If not, return False.
# 4. Recursively call on left and right children and return the AND result.
# Evaluate: Time O(N) to visit all nodes. Space O(H) for recursion stack.
# --------------------
class TreeNode():
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def is_univalued(root):
    # empty tree case
    if not root:
         return True

    if root.left and root.left.val != root.val:
        return False

    if root.right and root.right.val  != root.val:
        return False

    # recursive
    return is_univalued(root.left) and is_univalued(root.right)

# ============================================
# Problem 2: Binary Tree Height
# ============================================
# --- UMPIRE Steps ---
# Understand: Find the longest path from root to a leaf node. Empty tree is height 0.
# Match: DFS / Recursion.
# Plan:
# 1. Base Case: If root is None, return 0.
# 2. Recursive Step: Get height of left subtree and right subtree.
# 3. Return 1 + the maximum of the two children's heights.
# Evaluate: Time O(N) visits every node. Space O(H) for recursion stack.
# --------------------
def height(root):
    if not root:
        return 0

    left_height = height(root.left)
    right_height = height(root.right)

    return 1 + max(left_height, right_height)

# ============================================
# Problem 3: BST Insert
# ============================================
# --- UMPIRE Steps ---
# Understand: Input is a BST. Add a new node with key/val, or update val if key exists. Must maintain BST property (ordered by key).
# Match: BST Search / Recursion.
# Plan:
# 1. Base Case: If root is None, we reached the insertion spot. Return new TreeNode(key, val).
# 2. If key matches root.key, update root.val.
# 3. If key < root.key, recurse left: root.left = insert(root.left...).
# 4. If key > root.key, recurse right: root.right = insert(root.right...).
# 5. Return root to maintain connections.
# Evaluate: Time O(H) (searches one path). Space O(H) for recursion stack.
# --------------------
class TreeNode():
    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.val = value
        self.left = left
        self.right = right

def insert(root, key, value):
    if not root:
        return TreeNode(key, value)

    if key == root.key:
        root.val = value
    elif key < root.key:
        root.left = insert(root.left, key, value)
    else:
        root.right = insert(root.right, key, value)

    return root

# ============================================
# Problem 4: BST Remove I
# ============================================
# --- UMPIRE Steps ---
# Understand: Remove a node with a specific key from a BST. Handle 3 cases: leaf node, one child, two children.
# Match: BST Search / Recursion.
# Plan:
# 1. Find node: Recurse left if key < root.key, right if key > root.key.
# 2. If node found:
#    a. Case 1 (No children): Return None.
#    b. Case 2 (One child): Return the non-None child.
#    c. Case 3 (Two children): Find in-order successor (min of right subtree). Copy successor's key/val to current node. Recurse to delete successor from right subtree.
# Evaluate: Time O(H). Space O(H).
# --------------------

# ============================================
# Problem 5: BST In-order Successor
# ============================================
# --- UMPIRE Steps ---
# Understand: Find the node with the smallest key GREATER than the current node's key.
# Match: BST Properties.
# Plan:
# Case 1: Current node has a right child.
#    - Successor is the leftmost node in the right subtree.
# Case 2: Current node has NO right child.
#    - Start from root. Successor is the lowest ancestor where the current node is in its left subtree.
# Evaluate: Time O(H). Space O(1) (iterative).
# --------------------

# ============================================
# Problem 6: Merge Binary Trees
# ============================================
# --- UMPIRE Steps ---
# Understand: Overlay two trees. Sum values if nodes overlap. Use existing node if only one exists.
# Match: Pre-order Traversal (Recursion).
# Plan:
# 1. If root1 is None, return root2.
# 2. If root2 is None, return root1.
# 3. Both exist: Update root1.val += root2.val.
# 4. Recurse: root1.left = merge(root1.left, root2.left).
# 5. Recurse: root1.right = merge(root1.right, root2.right).
# 6. Return root1.
# Evaluate: Time O(N+M) where N,M are nodes in tree1, tree2. Space O(max(H1, H2)).
# --------------------



