class BinaryTree:
    def __init__ (self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

# O(n) time | O(1) space
def iterativeInOrderTraversal(node, callback):
    previousNode = None
    currentNode = node

    # 0. We run the loop until we reach the rightMost leaf
    while currentNode is not None:
        # 1. Traveling downwards 
        if previousNode is None or previousNode == currentNode.parent: # Traversing left down or we are the right leaf

            # 1.1. If we have left child then we need to explore them first. InOrder means we explore "left - current - right"
            if currentNode.left is not None:
                nextNode = currentNode.left 

            # 1.2. No left nodes. So we explore the currentNode and try to set the next node as currentNode.right. But if we are at a right leaf node then there is no further to explore so we assign the nextNode as our parentNode
            else:
                callback(currentNode) # All right nodes/childrens are explored here
                nextNode = currentNode.right if currentNode.right is not None else currentNode.parent

        # 2. Traveling UPWARDS from LEFT
        elif previousNode == currentNode.left: # Previous node is our currentNode's left child. That means we explored all the left subtree
            callback(currentNode)
            nextNode = currentNode.right if currentNode.right is not None else currentNode.parent

        # 3. Traveling UPWARDS from RIGHT
        elif previousNode == currentNode.right: # We already explored the right leaf and now need to explore upword
            nextNode = currentNode.parent

        # 4. Finally we update/move forward the previous and currentNode
        previousNode = currentNode
        currentNode = nextNode




        