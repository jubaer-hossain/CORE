import collections


class Solution(object):
    def findLeaves(self, root):
        depthToValues = collections.defaultdict(list)

        self.populateDepthToValuesUsingDFS(root, depthToValues)

        leaves = []
        for i in range(1, len(depthToValues) + 1):
            leaves.append(depthToValues[i])
        return leaves

    def populateDepthToValuesUsingDFS(self, node, depthToValues):
        if node is None:
            return 0
        
        leftSubtreeDepth = self.populateDepthToValuesUsingDFS(node.left, depthToValues)
        rightSubtreeDepth = self.populateDepthToValuesUsingDFS(node.right, depthToValues)

        currentTreeDepth = max(leftSubtreeDepth, rightSubtreeDepth) + 1
        depthToValues[currentTreeDepth].append(node.val)

        return currentTreeDepth