# O(n) time | O(d) space
def maxPathSum(tree):
    _, maxPath = maxPathSumFinder(tree)
    return maxPath

def maxPathSumFinder(tree):
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
    
    leftBrunchSum, leftPathSum = maxPathSumFinder(tree.left)
    rightBrunchSum, rightPathSum = maxPathSumFinder(tree.right)
    maxChildBrunchSum = max(leftBrunchSum, rightBrunchSum)

    value = tree.value
    maxBrunchSumWithRoot = max(maxChildBrunchSum + value, value)
    maxPathSumWithRoot = max(leftBrunchSum + value + rightBrunchSum, maxBrunchSumWithRoot)
    maxPathSum = max(leftPathSum, rightPathSum, maxPathSumWithRoot)

    return (maxBrunchSumWithRoot, maxPathSum)