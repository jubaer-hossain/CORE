# O(n) time | O(n) space
def allKindsOfNodeDepths(root):
    nodeCounts = {}
    addNodeCounts(root, nodeCounts)
    nodeDepths = {}
    addNodeDepths(root, nodeDepths, nodeCounts)
    return sumAllNodeDepths(root, nodeDepths)

def sumAllNodeDepths(node, nodeDepths):
    if node is None:
        return 0
    return sumAllNodeDepths(node.left, nodeDepths) + sumAllNodeDepths(node.right, nodeDepths) + nodeDepths[node] # Very basic node depth finder from left + right + currentNodeDepth

def addNodeDepths(node, nodeDepths, nodeCounts):
    nodeDepths[node] = 0 # Base case: when we're in a leaf node we want that node's depth to be 0

    if node.left is not None:
        addNodeDepths(node.left, nodeDepths, nodeCounts) # We first calculate the left subtree's node depths
        nodeDepths[node] += nodeDepths[node.left] + nodeCounts[node.left] # Then we add that left subtree's node depths and then add the number of nodes on that left subtree to calculate current node's depth
    if node.right is not None:
        addNodeDepths(node.right, nodeDepths, nodeCounts)
        nodeDepths[node] += nodeDepths[node.right] + nodeCounts[node.right]

def addNodeCounts(node, nodeCounts):
    nodeCounts[node] = 1 # Base case: when we're in a leaf node we want that node's count to be 1

    if node.left is not None:
        addNodeCounts(node.left, nodeCounts) # We first calculate the left subtree's node count
        nodeCounts[node] += nodeCounts[node.left] # Then add that node count from the dictionary to our current/parent node
    if node.right is not None:
        addNodeCounts(node.right, nodeCounts)
        nodeCounts[node] += nodeCounts[node.right]


# Recursive solution: O(n) time | O(h) space
def allKindsOfNodeDepths(root):
    return getTreeInfo(root).sumOfAllDepths

def getTreeInfo(tree):
    if tree is None:
        return TreeInfo(0, 0, 0)

    leftTreeInfo = getTreeInfo(tree.left)
    rightTreeInfo = getTreeInfo(tree.right)

    sumOfLeftDepths = leftTreeInfo.sumOfDepths + leftTreeInfo.numOfNodesInTree
    sumOfRightDepths = rightTreeInfo.sumOfDepths + rightTreeInfo.numOfNodesInTree

    numOfNodesInTree = 1 + leftTreeInfo.numOfNodesInTree + rightTreeInfo.numOfNodesInTree
    sumOfDepths = sumOfLeftDepths + sumOfRightDepths
    sumOfAllDepths = sumOfDepths + leftTreeInfo.sumOfAllDepths + rightTreeInfo.sumOfAllDepths # 16 + 6(left) + 2(right) + 2(left subtree sum of all depths)

    return TreeInfo(numOfNodesInTree, sumOfDepths, sumOfAllDepths)


class TreeInfo:
    def __init__(self, numOfNodesInTree, sumOfDepths, sumOfAllDepths):
        self.numOfNodesInTree = numOfNodesInTree
        self.sumOfDepths = sumOfDepths
        self.sumOfAllDepths = sumOfAllDepths

