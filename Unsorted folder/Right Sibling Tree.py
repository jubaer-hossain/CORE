# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right


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


# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def rightSiblingTree(root):
    mutate(root, None, False)
    return root

def mutate(node, parentNode, isLeftChild):
    if node is None:
        return

    # We back up the left and right node before changing the connections
    left, right = node.left, node.right

    # First mutate the left Subtree all the way till leaf node
    mutate(left, node, True)

    # Then mutate the currentNode
    if parentNode is None:
        node.right = None
    elif isLeftChild:
        if parentNode.right is None:
            node.right = None
        else:
            node.right = parentNode.right
    else: # Is a right child
        if parentNode.right is None:
            node.right = None
        else:
            node.right = parentNode.right.left

    mutate(right, node, False)