class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# O(n) time | O(h) space
def heightBalancedBinaryTree(tree):
    isBalanced, height = getTreeInfo(tree)
    return isBalanced

def getTreeInfo(node):
    if node is None:
        return (True, 0)
    
    leftSubTreeIsBalanced, leftSubTreeHeight = getTreeInfo(node.left)
    rightSubTreeIsBalanced, rightSubTreeHeight = getTreeInfo(node.right)

    isBalanced = (leftSubTreeIsBalanced and rightSubTreeIsBalanced and abs(leftSubTreeHeight - rightSubTreeHeight) <= 1)
    currentTreeHeight = max(leftSubTreeHeight, rightSubTreeHeight) + 1

    return (isBalanced, currentTreeHeight)