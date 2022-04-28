class BinaryTree:
    def __init__(self, value, left = None, right = None, parent = None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

# O(n) time | O(n) space
def findSuccessor(tree, node):
    inOrderTraversalOrder = getInOrderTraversal(tree)

    for idx, currentNode in enumerate(inOrderTraversalOrder):
        if currentNode == node and idx != len(inOrderTraversalOrder) - 1:
            return inOrderTraversalOrder[idx + 1]
    return None
        

def getInOrderTraversal(node, order = []):
    if node is None:
        return order
    getInOrderTraversal(node.left, order)
    order.append(node)
    getInOrderTraversal(node.right, order)

    return order

# More optimised approach
# O(n) time | O(h) space
def findSuccessor(tree, node):
    if node.right is not None:
        return getLeftMostChild(node.right)
    return getRightMostParent(node)

def getLeftMostChild(node):
    currentNode = node

    while currentNode.left is not None:
        currentNode = currentNode.left
    
    return currentNode

def getRightMostParent(node):
    currentNode = node

    while currentNode.parent is not None and currentNode.parent.right == currentNode:
        currentNode = currentNode.parent
    
    return currentNode.parent