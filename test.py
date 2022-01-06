# O(n) time | O(d) space -> Average case
def maxPathSum(tree):
    _, maxSum = maxPathSumFinder(tree)
    return maxSum

def maxPathSumFinder(tree):
    if tree is None:
        return (0, float("-inf"))

    leftBranchSum, leftMaxSum = maxPathSumFinder(tree.left)
    rightBranchSum, rightMaxSum = maxPathSumFinder(tree.right)
    maxChildBranchSum = max(leftBranchSum, rightBranchSum)

    value = tree.value
    maxBranchSumWithRoot = max(maxChildBranchSum + value, value)
    maxSumWithRoot = max(leftBranchSum + value + rightBranchSum, maxBranchSumWithRoot)
    maxSum = max(leftMaxSum, rightMaxSum, maxSumWithRoot)

    return (maxBranchSumWithRoot, maxSum)