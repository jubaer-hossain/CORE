class BinaryTree:
    def __init__ (self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

def iterativeInOrderTraversal(tree, callback):
    previousNode = None
    currentNode = tree
    while currentNode is not None:
        if previousNode is None or previousNode == currentNode.parent:
            if currentNode.left is not None:
                nextNode = currentNode.left
            else:
                callback(currentNode)
                nextNode = currentNode.right if currentNode.right is not None else currentNode.parent
        elif previousNode == currentNode.left:
            callback(currentNode)
            nextNode = currentNode.right if currentNode.right is not None else currentNode.parent
        else: # elif previousNode == currentNode.right
            callback(currentNode)
            nextNode = currentNode.parent
        previousNode = currentNode
        currentNode = nextNode