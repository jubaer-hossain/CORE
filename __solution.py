# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def rightSiblingTree(root):
    mutate(root, None, False)
    return root

# O(n) time | O(d) space
def mutate(node, parentNode, isLeftChild):
    if node is None:
        return

    # 1. We back up the left and right node before changing the connections
    left, right = node.left, node.right

    # 2. First mutate the left Subtree all the way till leaf node
    mutate(left, node, True)

    # 3. Then mutate the currentNode
    if parentNode is None: # Root node
        node.right = None
    elif isLeftChild: # Left child
        node.right = parentNode.right
    else: # Is a right child
        if parentNode.right is None: # We need to check this because we are trying to access parentNode.right.left. And if "parentNode.right is None" then it will give an error
            node.right = None
        else:
            node.right = parentNode.right.left

    # 4. Finally mutate the right Subtree
    mutate(right, node, False)


    