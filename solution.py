def allKindsOfNodeDepths(root):
    # 1. Counting all nodes on each individual subtree
    nodeCounts = {}
    getNodeCounts(root, nodeCounts)

    # 2. Counting nodeDepths of each node on individual subtree
    nodeDepths = {}
    getNodeDepths(root, nodeCounts, nodeDepths)

    # 3. Summing up all nodeDepths from all subtree
    return sumAllNodeDepths(root, nodeDepths)


# 1. Single pass algorithm to count & store all nodes in each subtree of a binary tree
def getNodeCounts(node, nodeCounts):
    nodeCounts[node] = 1 # Because currentNode is 1 node within the tree

    if node.left is not None:
        getNodeCounts(node.left, nodeCounts)
        nodeCounts[node] += nodeCounts[node.left]

    if node.right is not None:
        getNodeCounts(node.right, nodeCounts)
        nodeCounts[node] += nodeCounts[node.right]


# 2. Single pass algorithm to count all node Depths in each subtree
def getNodeDepths(node, nodeCounts, nodeDepths):
    nodeDepths[node] = 0

    if node.left is not None:
        getNodeDepths(node.left, nodeCounts, nodeDepths)
        nodeDepths[node] += nodeDepths[node.left] + nodeCounts[node.left]

    if node.right is not None:
        getNodeDepths(node.right, nodeCounts, nodeDepths)
        nodeDepths[node] += nodeDepths[node.right] + nodeCounts[node.right]


# 3. Summing up all nodeDepths from all subtree. Again single pass
def sumAllNodeDepths(node, nodeDepths):
    if node is None:
        return 0
    return sumAllNodeDepths(node.left, nodeDepths) + sumAllNodeDepths(node.right, nodeDepths) + nodeDepths[node]



class TreeInfo:
    def __init__(self, nodeCountsInSubtree, sumOfDepths, sumOfAllDepths):
        self.nodeCountsInSubtree = nodeCountsInSubtree
        self.sumOfDepths = sumOfDepths
        self.sumOfAllDepths = sumOfAllDepths
        

def allKindsOfNodeDepths(root):
    return getTreeInfo(root).sumOfAllDepths

