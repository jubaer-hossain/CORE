# O(n) time | O(log(n)) space
def maxPathSum(tree):
    _, maxSum = findMaxSum(tree)
    return maxSum

def findMaxSum(tree):
    if tree is None:
        return (0, float("-inf"))
    """
    Because let's say we have a tree that has only one node as -2. 
    In that case if it returns "0" which is a bigger number than -2 it will return the maxPathSum as 0. 
    But that is an incorrect value. 
    """

    leftMaxSumAsBranch, leftSubtreeSum = findMaxSum(tree.left)
    rightMaxSumAsBranch, rightSubtreeSum = findMaxSum(tree.right)

    # Branch
    maxChildSumAsBranch = max(leftMaxSumAsBranch, rightMaxSumAsBranch) # Max branch sum without root

    # Branch with/without root
    value = tree.value
    maxSumAsBranch = max(maxChildSumAsBranch + value, value) # max branch sum Including the root node
    maxSumAsRootNode = max(leftMaxSumAsBranch + value + rightMaxSumAsBranch, maxSumAsBranch) # Sometimes (leftBranch + node.val + rightBranch) could be less than only (node.val + left/rightBranchSum)


    # Final maxPathSum
    maxPathSum = max(leftSubtreeSum, rightSubtreeSum, maxSumAsRootNode) # LeftSubtree or rightSubtree or a path within the root

    return (maxSumAsBranch, maxPathSum)

"""

      10
     /   \
    5     15
   / \   /   \
  2   5 13   22
 /      / \
1      12 14

"""