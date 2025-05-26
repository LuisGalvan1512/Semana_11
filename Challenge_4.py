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

def build_bst(arr):
    if not arr:
        return None
    root = TreeNode(arr[0])
    for v in arr[1:]:
        insert_into_bst(root, v)
    return root

def kth_smallest(root, k):
    stack = []
    current = root
    count = 0

    while stack or current:
        while current:
            stack.append(current)
            current = current.left
        node = stack.pop()
        count += 1
        if count == k:
            return node.val
        current = node.right
    return None


# ✅ Test cases
# Test 1: Kth smallest in balanced BST
# BST: [3, 1, 4, 2] -> sorted: [1, 2, 3, 4]
# k = 2
# Expected: 2
print(kth_smallest(build_bst([3, 1, 4, 2]), 2) == 2)  # 🎯 Second smallest

# Test 2: First smallest (minimum)
# BST: [5, 3, 7, 2, 4, 6, 8]
# k = 1
# Expected: 2
print(kth_smallest(build_bst([5, 3, 7, 2, 4, 6, 8]), 1) == 2)  # 📊 Minimum value

# Test 3: Last element (maximum)
# BST: [5, 3, 7, 2, 4, 6, 8]
# k = 7
# Expected: 8
print(kth_smallest(build_bst([5, 3, 7, 2, 4, 6, 8]), 7) == 8)  # 📈 Maximum value

# Test 4: Middle element
# BST: [4, 2, 6, 1, 3, 5, 7]
# k = 4
# Expected: 4
print(kth_smallest(build_bst([4, 2, 6, 1, 3, 5, 7]), 4) == 4)  # 🔗 Middle element

# Test 5: Single node tree
# BST: [10]
# k = 1
# Expected: 10
print(kth_smallest(build_bst([10]), 1) == 10)  # 🌱 Single node