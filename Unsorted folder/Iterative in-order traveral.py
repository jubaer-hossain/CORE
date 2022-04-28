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
        if previousNode is None or previousNode == currentNode.parent: # Traversing left down or we are the right leaf
            if currentNode.left is not None:
                nextNode = currentNode.left # If a node have left child then we need to explore further down
            else:
                callback(currentNode) # no left node. So we explore the currentNode and try to set the next node as currentNode.right. But if we are at a right leaf node then there is no further to explore so we assign the nextNode as our parentNode
                nextNode = currentNode.right if currentNode.right is not None else currentNode.parent
        elif previousNode == currentNode.left: # Previous node is our currentNode's left child. That means we explored all the left subtree
            callback(currentNode)
            nextNode = currentNode.right if currentNode.right is not None else currentNode.parent
        elif previousNode == currentNode.right: # We already explored the right leaf and now need to explore upword
            nextNode = currentNode.parent
        
        previousNode = currentNode
        currentNode = nextNode