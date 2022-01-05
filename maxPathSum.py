# O(n) time | O(log(n)) space
def maxPathSum(tree):
    _, maxSum = findMaxSum(tree)
    return maxSum

def findMaxSum(tree):
    if tree is None:
        return (float(-"inf"), float("-inf"))
    """
    Because let's say we have a tree that has only one node as -2. 
    In that case if it returns "0" which is a bigger number than -2 it will return the maxPathSum as 0. 
    But that is an incorrect value. 
    return (float("-inf"), float("-inf")) will work too 
    cause if the tree has any brunch then returning 0 will be neutralised in the next Recursive call
    where the tree has actually a value
    """

    leftMaxSumAsBranch, leftMaxPathSum = findMaxSum(tree.left)
    rightMaxSumAsBranch, rightMaxPathSum = findMaxSum(tree.right)
    maxChildSumAsBranch = max(leftMaxSumAsBranch, rightMaxSumAsBranch)

    value = tree.value
    maxSumAsBranch = max(maxChildSumAsBranch + value, value) # Including the root node
    maxSumAsRootNode = max(leftMaxSumAsBranch + value + rightMaxSumAsBranch, maxSumAsBranch)
    maxPathSum = max(leftMaxPathSum, rightMaxPathSum, maxSumAsRootNode)

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