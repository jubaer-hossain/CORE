# O(nlog(n)) time | O(n) space
def rightSmallerThan(array):
    if len(array) == 0:
        return []

    lastIdx = len(array) - 1
    bst = SpecialBST(array[lastIdx], lastIdx, 0) # totalSmallNodesAtInsert = 0 by default
    for i in reversed(range(len(array) - 1)): # From the second last element(4). [8, 5, 11, -1, 3, 4, 2]. len = 7
        bst.insert(array[i], i)

    rightSmallerCounts = array[:]
    getRightSmallerCounts(bst, rightSmallerCounts)
    return rightSmallerCounts


def getRightSmallerCounts(bst, rightSmallerCounts):
    if bst is None:
        return
    rightSmallerCounts[bst.idx] = bst.totalSmallNodesAtInsert
    getRightSmallerCounts(bst.left, rightSmallerCounts)
    getRightSmallerCounts(bst.right, rightSmallerCounts)


class SpecialBST:
    def __init__ (self, value, idx, totalSmallNodesAtInsert):
        self.value = value
        self.idx = idx
        self.totalSmallNodesAtInsert = totalSmallNodesAtInsert
        self.leftSubtreeSize = 0
        self.left = None
        self.right = None

    def insert(self, value, idx, totalSmallNodesAtInsert = 0):
        if value < self.value:
            self.leftSubtreeSize += 1
            if self.left is None:
                self.left = SpecialBST(value, idx, totalSmallNodesAtInsert)
            else:
                self.left.insert(value, idx, totalSmallNodesAtInsert) # We need
                # totalSmallNodesAtInsert while traversing left and right deep 
                # into the tree
        else:
            totalSmallNodesAtInsert += self.leftSubtreeSize # Need to be careful about this value
            if value > self.value:
                totalSmallNodesAtInsert += 1 # Cause equal values don't count

            if self.right is None:
                self.right = SpecialBST(value, idx, totalSmallNodesAtInsert)
            else:
                self.right.insert(value, idx, totalSmallNodesAtInsert)



# Approach-2: Using less space
# O(nlog(n)) time | O(n) space
def rightSmallerThan(array):
    if len(array) == 0:
        return []

    rightSmallerCounts = array[:]

    lastIdx = len(array) - 1
    bst = SpecialBST(array[lastIdx]) # Cause we are traversing from the right/end
    # So need to create the first bst with the last value of the array
    rightSmallerCounts[lastIdx] = 0

    for i in reversed(range(len(array) - 1)):
        bst.insert(array[i], i, rightSmallerCounts)

    return rightSmallerCounts

class SpecialBST:
    def __init__(self, value):
        self.value = value
        self.leftSubtreeSize = 0
        self.left = None
        self.right = None

    def insert(self, value, idx, rightSmallerCounts, totalSmallNodesAtInsert = 0):
        if value < self.value:
            self.leftSubtreeSize += 1

            if self.left is None:
                self.left = SpecialBST(value)
                rightSmallerCounts[idx] = totalSmallNodesAtInsert
            else:
                self.left.insert(value, idx, rightSmallerCounts, totalSmallNodesAtInsert)
        else:
            totalSmallNodesAtInsert += self.leftSubtreeSize # Forgot to add this every time
            if value > self.value:
                totalSmallNodesAtInsert += 1

            if self.right is None:
                self.right = SpecialBST(value)
                rightSmallerCounts[idx] = totalSmallNodesAtInsert
            else:
                self.right.insert(value, idx, rightSmallerCounts, totalSmallNodesAtInsert)




def rightSmallerThan(array):
    if len(array) == 0:
        return array

    lastIdx = len(array) - 1

    root = SpecialBST(array[lastIdx], lastIdx, 0) # 0 is for elements to the right

    for i in reversed(range(len(array) - 1)):
        root.insert(array[i], i, 0)

    result = array[:]
    getRightSmallerCounts(root, result)
    return result

def getRightSmallerCounts(node, result):
    if node is None:
        return

    result[node.idx] = node.smallerElementsAtInsert

    getRightSmallerCounts(node.left, result)
    getRightSmallerCounts(node.right, result)


class SpecialBST:
    def __init__(self, value, idx, smallerElementsAtInsert):
        self.value = value
        self.idx = idx
        self.smallerElementsAtInsert = smallerElementsAtInsert

        self.leftSubtreeSize = 0

        self.left = None
        self.right = None

    def insert(self, value, idx, smallerElementsAtInsert = 0):
        # If the value fits in the left Subtree
        if value < self.value:
            self.leftSubtreeSize += 1

            # If we are at leaf node, then create a new Node
            if self.left is None:
                self.left = SpecialBST(value, idx, smallerElementsAtInsert)

            # Otherwise we pass down the current value to be inserted at the leftSubtree where it fits
            else:
                self.left.insert(value, idx, smallerElementsAtInsert)

        # Otherwise the value must stores in the right Subtree
        else:
            smallerElementsAtInsert += self.leftSubtreeSize
            # Edge case: When the currentValue is strictly larger than the currentNode which means currentNode's value is smaller so we need to add an extra 1 to the result
            if value > self.value:
                smallerElementsAtInsert += 1

            # Inserting the node on right Subtree
            if self.right is None:
                self.right = SpecialBST(value, idx, smallerElementsAtInsert)
            else:
                self.right.insert(value, idx, smallerElementsAtInsert)




                