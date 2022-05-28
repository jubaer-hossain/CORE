# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right



class TreeInfo:
    def __init__(self, n, l):
        self.n = n
        self.l = l

        
def findKthLargestValueInBst(tree, k):
    treeInfo = TreeInfo(0, -1)
    reverseInOrderTraversal(tree, k, treeInfo)
    return treeInfo.l







def reverseInOrderTraversal(node, k, treeInfo):
    if node is None or treeInfo.n >= k:
        return


    reverseInOrderTraversal(node.right, k, treeInfo)

    if treeInfo.n < k:
        treeInfo.n += 1
        treeInfo.l = node.value

        reverseInOrderTraversal(node.left, k, treeInfo)