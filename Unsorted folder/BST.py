class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Average: O(log(n)) time | O(1) space
    # Worst: O(n) time | O(1) space -> If we have a tree that have only a chain
    def insert(self, value):
        currentNode = self

        while True:
            if value < currentNode.value:
                if currentNode.left is None:
                    currentNode.left = BST(value)
                    break
                else:
                    currentNode = currentNode.left
            elif value > currentNode.value:
                if currentNode.right is None:
                    currentNode.right = BST(value)
                    break
                else:
                    currentNode = currentNode.right
            else:
                if currentNode.right is None:
                    currentNode.right = BST(value)
                    break
                else: 
                    currentNode = currentNode.right
        return self

    # Average: O(log(n)) time | O(1) space
    # Worst: O(n) time | O(1) space
    def contains(self, value):
        currentNode = self

        while currentNode is not None:
            if value < currentNode.value:
                currentNode = currentNode.left
            elif value > currentNode.value:
                currentNode = currentNode.right
            else:
                return True
        return False


    # Average: O(log(n)) time | O(1) space
    # Worst: O(n) time | O(1) space
    def remove(self, value, parentNode = None):
        currentNode = self
        while currentNode is not None:
            # Searching for the value
            if value < currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.left
            elif value > currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.right
            else:
                # Target Node that have two child. It could be Root node or Any node
                if currentNode.left is not None and currentNode.right is not None:
                    currentNode.value = currentNode.right.getMinValue() # currentNode.value = 12 now
                    currentNode.right.remove(currentNode.value, currentNode) # currentNode.right.remove(12, BST(15))
                # Remove Root node and the Root node only have one child
                elif parentNode is None:
                    if currentNode.left is not None: # If that one child is the left child
                        currentNode.value = currentNode.left.value
                        currentNode.right = currentNode.left.right # Node that we are updating currentNode.right first becuase if we update currentNode.left first then we are overwriting the values and can not update currentNode.right later
                        currentNode.left = currentNode.left.left
                    elif currentNode.right is not None:
                        currentNode.value = currentNode.right.value
                        currentNode.left = currentNode.right.left
                        currentNode.right = currentNode.right.right
                    else:
                        currentNode.value = None
                # Target Node that have only left child and it is not the root
                elif parentNode.left == currentNode:
                    parentNode.left = currentNode.left if currentNode.left is not None else currentNode.right
                # Target Node that have only right child and it is not the root
                elif parentNode.right == currentNode:
                    parentNode.right = currentNode.left if currentNode.left is not None else currentNode.right
                break
        return self # Not necessary for the BST logic

    def getMinValue(self): # Is only called on the right Subtree
        currentNode = self
        while currentNode.left is not None: # Travel until we reach an empty left node. Mainly traveling to the smallest left node
            currentNode = currentNode.left
        return currentNode.value
        
        
"""

      10
     /   \
    5     15
   / \   /   \
  2   5 13   22
 /      / \
1      12 14

"""

# Test code
