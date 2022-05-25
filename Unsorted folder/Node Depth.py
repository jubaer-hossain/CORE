class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Recursive approach
"""
Sudo:
Base case: Leaf node -> return 0
For in each node's depth is basically previous depth + 1.
So the recursive function will be depth + left, current depth + 1, right, current depth + 1
"""

# O(n) time | O(log(n)) space
def nodeDepths(root, depth = 0):
    if root is None:
        return 0
    return depth + nodeDepths(root.left, depth + 1) + nodeDepths(root.right, depth + 1)

# Iterative approach
# O(n) time | O(h) space
"""
Sudo:
Use a list of dictionary that stores "node" and "depth"
Use LIFO order pop() and append() and calculate depth until the stack/list is empty

Corner case: if node is None then continue
"""

# O(n) time | O(h) space
def nodeDepths(root):
    sumOfDepths = 0
    stack = [{"node": root, "depth": 0}]
    
    while len(stack) > 0:
        nodeInfo = stack.pop() # List in python is LIFO for append() and pop()
        node, depth = nodeInfo["node"], nodeInfo["depth"] # Grabbing the actual value from the dictionary
        
        if node is None:
            continue
        sumOfDepths += depth

        stack.append({"node": node.left, "depth": depth + 1})
        stack.append({"node": node.right, "depth": depth + 1})
    
    return sumOfDepths



