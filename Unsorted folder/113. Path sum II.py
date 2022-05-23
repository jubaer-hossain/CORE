# Approach-1: Top down recursive DFS backtracking
"""Algorithm:
1. We call the DFS on the root node
2. If we are on a Leaf node, append the current Path with result: result.append(list(currentPath))
3. If we are not on a Leaf node, call DFS on left and right node
4. Remove node from currentPath and subtract node.value from currentRunningSum once a node is
processed. Basically backtracking
So the function will return the result array when it hits the None node. So the result will be updated
once we are at the right most None node(end of the tree)
"""

# O(n^2) time | O(n) space without output
class Solution(object):
    def pathSum(self, root, targetSum):
        result = []
        currentPath = []
        self.getPathSum(root, targetSum, 0, currentPath, result)
        return result

    def getPathSum(self, node, targetSum, currentRunningSum, currentPath, result):
        if node is not None:
            currentRunningSum += node.val
            currentPath.append(node.val)

            if node.left is None and node.right is None: # Leaf node
                if currentRunningSum == targetSum:
                    result.append(list(currentPath))
            else:
                # First the full left subtree is processed until None node and then
                # it backtracks and removes all the values from the currentPath and updates
                # currentRunningSum and then start executing the right subtree
                self.getPathSum(node.left, targetSum, currentRunningSum, currentPath, result)
                self.getPathSum(node.right, targetSum, currentRunningSum, currentPath, result)
            
            # Once a node is processed we have to remove it from currentPath
            # and also delete the currentRunningSum
            currentPath.pop()
            currentRunningSum -= node.val
        return result # Only returns result when we are at a None node


# Approach-2: Subtracting targetSum and using recursive DFS backtracking
# O(n^2) time | O(n) space
class Solution:
    def pathSum(self, root, targetSum):
        result = []
        self.getTargetSum(root, targetSum, [], result)
        return result
    
    def getTargetSum(self, node, targetSum, currentPath, result):
        if node is None:
            return result # Returning None will also work since arrays in python
            # is passed by reference
        
        targetSum -= node.val
        currentPath.append(node.val)

        if node.left is None and node.right is None:
            if targetSum == 0:
                result.append(list(currentPath))
        else:
            self.getTargetSum(node.left, targetSum, currentPath, result)
            self.getTargetSum(node.right, targetSum, currentPath, result)
        currentPath.pop() # Backtracking/removing the node once it's processed 
        # so that right subtrees do not have left subtree nodes on their path




        