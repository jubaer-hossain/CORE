class BinaryTree:
    def __init__ (self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

# O(n) time | O(1) space
def iterativeInOrderTraversal(tree, callback):
    previousNode = None
    currentNode = tree

    while currentNode is not None:
        if previousNode is None or currentNode.parent == previousNode: # If there is a left child
            if currentNode.left is not None:
                nextNode = currentNode.left
            else:
                callback(currentNode)
                nextNode = currentNode.right if currentNode.right is not None else currentNode.parent
        elif previousNode == currentNode.left: # If we are back up from the left child
            callback(currentNode)
            nextNode = currentNode.right if currentNode.right is not None else currentNode.parent
        else: # previousNode == currentNode.right. If we are coming back up from the right child
            nextNode = currentNode.parent
        previousNode = currentNode
        currentNode = nextNode