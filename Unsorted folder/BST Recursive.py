class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Average: O(log(n)) time | O(log(n)) space
    # Worst: O(n) time | O(n) space
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
        return self

    # Average: O(log(n)) time | O(1) space
    # Worst: O(n) time | O(1) space
    def contains(self, value):
        if value < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(value)
        elif value > self.value:
            if self.right is None:
                return False
            else:
                return self.right.contains(value)
        else:
            return True

    # Average: O(log(n)) time | O(log(n)) space
    # Worst: O(n) time | O(n) space
    def remove(self, value, parent = None):
        if value < self.value:
            if self.left is not None:
                self.left.remove(value, self)
        elif value > self.value:
            if self.right is not None:
                self.right.remove(value, self)
        else: # Actual remove logics
            if self.left is not None and self.right is not None:
                self.value = self.right.getMindValue()
                self.right.remove(self.value, self)
            elif parent is None:
                if self.left is not None:
                    self.value = self.left.value
                    self.right = self.left.right
                    self.left = self.left.left
                if self.right is not None:
                    self.value = self.right.value
                    self.left = self.right.left
                    self.right = self.right.right
                else:
                    self.value = None # Binary tree have only one node
            # elif self.left.value == value:
            elif parent.left == self:
                parent.left = self.left if self.left is not None else self.right
            elif parent.right == self:
                parent.right = self.left if self.left is not None else self.right
        return self

    def getMinValue(self):
        if self.left is None:
            return self.value
        else:
            return self.left.getMinValue()



# Iterative approach
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # O(n)/(log(n)) time | O(1) space 
    def insert(self, value):
        currentNode = self

        while True:
            # 1. Smaller than currentNode -> Go to left Subtree
            if value < currentNode.value:
                # 1.1. If we reach a Leaf node -> Create a new BST node and insert the currentNode as left child
                if currentNode.left is None:
                    currentNode.left = BST(value)
                    break
                else:
                    currentNode = currentNode.left

            # 2. Larger than currentNode -> Go to right Subtree
            else:
                # 2.1. If we reach a Leaf node -> 
                if currentNode.right is None:
                    currentNode.right = BST(value)
                    break
                else:
                    currentNode = currentNode.right
        return self

    # O(n)/(log(n)) time | O(1) space 
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

    # O(n)/(log(n)) time | O(1) space 
    def remove(self, value, parentNode = None):
        currentNode = self

        while currentNode is not None:
            # Step-1: Finding the targetNode that we need to remove
            if value < currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.left
            elif value > currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.right

            # Step-2: Removing the node
            else:
                # Case-1: currentNode(node to remove) has both left and right child. Could be root node as well
                if currentNode.left is not None and currentNode.right is not None:
                    # Replace the currentNode's value with the rightSubtree leftMost value. In other words, next min value in the tree
                    currentNode.value = currentNode.right.getMinValue()

                    # Call remove() method on the rightSubtree to remove the leftMost node. Must pass a parent
                    currentNode.right.remove(currentNode.value, currentNode)

                # Case-2: Removing the Root node that has only Left or Right Subtree
                elif parentNode is None:
                    if currentNode.left is not None:
                        currentNode.value = currentNode.left.value # Overwrite values
                        currentNode.right = currentNode.left.right # Link right child first
                        currentNode.left = currentNode.left.left # Then link left child
                    elif currentNode.right is not None:
                        currentNode.value = currentNode.right.value
                        currentNode.left = currentNode.right.left
                        currentNode.right = currentNode.right.right
                    else: # If the tree only have one node
                        return None

                # Case-3: Removing a node that has LESS THAN TWO child and a LEFT child of a node
                elif parentNode.left == currentNode:
                    parentNode.left = currentNode.left if currentNode.left is not None else currentNode.right
                elif parentNode.right == currentNode:
                    parentNode.right = currentNode.left if currentNode.left is not None else currentNode.right

                # Once we remove the node, we break out of the while loop
                break
        return self
                    

    # Returns the min value of a Binary Search Subtree
    def getMinValue(self):
        currentNode = self

        # We traverse in the left subtree cause in a BST usually the leftMost leaf is the smallest
        # Note that we don't check currentNode is not None. We check currentNode.left is not None. Which means we are gonna stop at a Leaf Node
        while currentNode.left is not None:
            currentNode = currentNode.left

        return currentNode.value 


