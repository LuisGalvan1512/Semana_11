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

build_degenerate_bst = build_bst

def bst_to_dll(root):

    if not root:
        return None
    def link(a, b):
        a.right = b
        b.left = a

    stack, node = [], root
    head = tail = None

    while stack or node:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        if head is None:
            head = node
        if tail:
            link(tail, node) 
        tail = node
        node = node.right
    link(tail, head)
    return head

def validate_circular_dll(head, expected):
    if not expected:
        return head is None
    vals = []
    curr = head
    for _ in range(len(expected)):
        vals.append(curr.val)
        curr = curr.right
    return vals == expected and curr is head





# ✅ Test cases
# Test 1: Simple BST
# BST:   2        DLL: 1 <-> 2 <-> 3 (circular)
#       / \
#      1   3
head1 = bst_to_dll(build_bst([2, 1, 3]))
print(validate_circular_dll(head1, [1, 2, 3]) == True)  # 🔗 Simple conversion

# Test 2: Larger BST
# BST: [4, 2, 6, 1, 3, 5, 7]
# DLL: 1 <-> 2 <-> 3 <-> 4 <-> 5 <-> 6 <-> 7 (circular)
head2 = bst_to_dll(build_bst([4, 2, 6, 1, 3, 5, 7]))
print(validate_circular_dll(head2, [1, 2, 3, 4, 5, 6, 7]) == True)  # 📊 Complex conversion

# Test 3: Single node
# BST: 5
# DLL: 5 (points to itself)
head3 = bst_to_dll(build_bst([5]))
print(validate_circular_dll(head3, [5]) == True)  # 🌱 Single node

# Test 4: Degenerate BST (like linked list)
# BST: 1 -> 2 -> 3 -> 4
# DLL: 1 <-> 2 <-> 3 <-> 4 (circular)
head4 = bst_to_dll(build_degenerate_bst([1, 2, 3, 4]))
print(validate_circular_dll(head4, [1, 2, 3, 4]) == True)  # 📈 Degenerate case

# Test 5: Empty tree
# BST: None
# DLL: None
head5 = bst_to_dll(None)
print(head5 is None)  # 📭 Empty tree
