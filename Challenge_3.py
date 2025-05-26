class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert_into_bst(root, val):
    if val < root.val:
        if root.left:
            insert_into_bst(root.left, val)
        else:
            root.left = TreeNode(val)
    else:
        if root.right:
            insert_into_bst(root.right, val)
        else:
            root.right = TreeNode(val)

def build_tree(arr):
    if not arr:
        return None
    root = TreeNode(arr[0])
    for v in arr[1:]:
        insert_into_bst(root, v)
    return root

def build_invalid_tree1():
    root = TreeNode(5)
    root.left = TreeNode(6)  
    root.right = TreeNode(7)
    return root

def build_invalid_tree2():
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(4)
    return root

def is_valid_bst(root):
    def helper(node, low, high):
        if not node:
            return True
        if node.val <= low or node.val >= high:
            return False
        return helper(node.left, low, node.val) and helper(node.right, node.val, high)

    return helper(root, float('-inf'), float('inf'))


# ✅ Test cases
# Test 1: Valid BST
# Tree:    5
#         / \
#        3   7
#       / \ / \
#      2  4 6  8
print(is_valid_bst(build_tree([5, 3, 7, 2, 4, 6, 8])) == True)  # ✅ Valid BST

# Test 2: Invalid BST - left violation
# Tree:    5
#         / \
#        6   7  (6 > 5, violates BST)
print(is_valid_bst(build_invalid_tree1()) == False)  # ❌ Left violation

# Test 3: Invalid BST - right violation
# Tree:    5
#         / \
#        3   4  (4 < 5, violates BST)
print(is_valid_bst(build_invalid_tree2()) == False)  # ❌ Right violation

# Test 4: Single node
# Tree: 42
print(is_valid_bst(build_tree([42])) == True)  # 🌱 Single node valid

# Test 5: Empty tree
# Tree: None
print(is_valid_bst(None) == True)  # 📭 Empty tree valid
