"""
Sudocode: 
1. If no parent then right is None
2. If left child then parent.right
3. If right child then first check if parent.right is None.
If not None then parent.right.left
"""

# O(n) time | O(d) space
def rightSiblingTree(root):
    mutate(root, None, None)
    return root

def mutate(node, parent, isLeftChild):
    if node is None:
        return

    left, right = node.left, node.right
    mutate(left, node, True)
    if parent is None:
        node.right = None
    elif isLeftChild:
        node.right = parent.right
    else:
        if parent.right is None:
            node.right = None
        else:
            node.right = parent.right.left
    mutate(right, node, False)