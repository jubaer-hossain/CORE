class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def binaryTreeDiameter(tree):
    maxDiameter, _ = getTreeInfo(tree)
    return maxDiameter

def getTreeInfo(tree):
    if tree is None:
        return (0, 0) # currentDiameter, currentHeight
    
    leftTreeDiameter, leftTreeHeight = getTreeInfo(tree.left)
    rightTreeDiameter, rightTreeHeight = getTreeInfo(tree.right)

    longestPathThroughRoot = leftTreeHeight + rightTreeHeight
    maxSubTreeDiameter = max(leftTreeDiameter, rightTreeDiameter)
    
    currentMaxDiameter = max(longestPathThroughRoot, maxSubTreeDiameter)
    currentMaxHeight = 1 + max(leftTreeHeight, rightTreeHeight)

    return (currentMaxDiameter, currentMaxHeight)