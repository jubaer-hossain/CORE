class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# O(n) time because we are traversing all the node once
"""
O(n) space. Because we will never have
more than log(n) frames in the call stack
and no more than n/2 leaf node on a balanced
binary tree
"""
def branchSums(root):
    result = []
    calculateBranchSum(root, result, 0) # Root node has no running sum
    return result

def calculateBranchSum(node, result, currntRunningSum):
    if node is None:
        return
    
    currntRunningSum += node.value
    if node.left is None and node.right is None:
        result.append(currntRunningSum)
        return
    
    calculateBranchSum(node.left, result, currntRunningSum)
    calculateBranchSum(node.right, result, currntRunningSum)