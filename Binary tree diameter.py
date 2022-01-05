# O(n) time | O(h) space(average), O(n) space(worst)
def binaryTreeDiameter(tree):
    return getTreeInfo(tree).diameter

def getTreeInfo(tree):
    if tree is None:
        return TreeInfo(0, 0)
    
    leftTreeInfo = getTreeInfo(tree.left)
    rightTreeInfo = getTreeInfo(tree.right)

    longestPathThroughRoot = leftTreeInfo.height + rightTreeInfo.height
    maxSubTreeDiameter = max(leftTreeInfo.diameter, rightTreeInfo.diameter)
    currentMaxDiameter = max(longestPathThroughRoot, maxSubTreeDiameter)
    currentMaxHeight = 1 + max(leftTreeInfo.height, rightTreeInfo.height)

    return TreeInfo(currentMaxDiameter, currentMaxHeight)

class TreeInfo:
    def __init__(self, diameter, height):
        self.diameter = diameter
        self.height = height

class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# Solution without using objects
def binaryTreeDiameter(tree):
    pass

def getTreeInfo(tree):
    if tree is None:
        return (0, 0)
    
    leftTreeDiameter, leftTreeHeight = getTreeInfo(tree.left)
    