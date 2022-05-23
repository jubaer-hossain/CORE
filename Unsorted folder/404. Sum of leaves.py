# O(n) time | O(h) space
class Solution(object):
    def sumOfLeftLeaves(self, root):
        runningSum = 0
        leftLeavesSum = self.getLeavesSum(root, False, runningSum)
        return leftLeavesSum
    
    def getLeavesSum(self, node, isLeftChild, runningSum):
        if node is None:
            return 0
        
        if node.left is None and node.right is None: # Is leaf node
            if isLeftChild:
                return node.val
            else:
                return 0
        
        leftSubtreeSum = self.getLeavesSum(node.left, True, runningSum)
        rightSubtreeSum = self.getLeavesSum(node.right, False, runningSum)

        return leftSubtreeSum + rightSubtreeSum


    