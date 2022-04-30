import collections

# O(n) time | O(n) space
class Solution(object):
    def findLeaves(self, root):
        depthToValues = collections.defaultdict(list) # To map all the nodes to a dictionary where key will be height and value will be a list of leaf values
        self.getDepthForEachNode(root, depthToValues)
        
        result = []
        """
        Started from index 1 because depthToValues dictionary has 3 elements 
        but starts from 1 and ends at 3. So since we are accessing dictionary values 
        through i, we need to loop from 1 to len+1 -> More precicely indices of 1, 2, 3
        range(1, 4) means 1, 2, 3
        """
        for i in range(1, len(depthToValues) + 1): 
            result.append(depthToValues[i])
        return result

    def getDepthForEachNode(self, root, depthToValues):
        if root is None:
            return 0
        leftSubtreeDepth = self.getDepthForEachNode(root.left, depthToValues)
        rightSubtreeDepth = self.getDepthForEachNode(root.right, depthToValues)
        
        currentTreeDepth = max(leftSubtreeDepth, rightSubtreeDepth) + 1
        depthToValues[currentTreeDepth].append(root.val)

        return currentTreeDepth


# More clean code
class Solution(object):
    def findLeaves(self, root):
        depthToValues = collections.defaultdict(list) # To map all the nodes to a dictionary where key will be height and value will be a list of leaf values
        self.getDepthForEachNode(root, depthToValues)
        
        return depthToValues.values()

    def getDepthForEachNode(self, root, depthToValues):
        if root is None:
            return 0
        leftSubtreeDepth = self.getDepthForEachNode(root.left, depthToValues)
        rightSubtreeDepth = self.getDepthForEachNode(root.right, depthToValues)
        
        currentTreeDepth = max(leftSubtreeDepth, rightSubtreeDepth) + 1
        depthToValues[currentTreeDepth].append(root.val)
        return currentTreeDepth
