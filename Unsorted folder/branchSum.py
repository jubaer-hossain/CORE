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

# My own solution after 2 months
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def branchSums(tree):
	result = []
	findSum(tree, result, 0) # We are passing the entire array and it's updating on each time we are hitting a leaf node
	return result

def findSum(node, result, currentSum):
	if node is None:
		return # By returning we are only 
	
	currentSum += node.value
	
	if node.left is None and node.right is None:
		result.append(currentSum)
	else: # Whether we put it after else or without any else, doesn't really matter because of the logic design
		findSum(node.left, result, currentSum)
		findSum(node.right, result, currentSum)
	
	currentSum -= node.value # Doesn't really matter if we subtract the value or not after processing a node. Because when calling a child node, we are passing the currentSum value and it doesn't need to be modified after we process a full Root to Leaf path

 