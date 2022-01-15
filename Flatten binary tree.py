# O(n) time | O(n) space
def flattenBinaryTree(root):
    inOrderNodes = getNodesInOrder(root, [])

    for i in range(0, len(inOrderNodes) - 1):
        leftNode = inOrderNodes[i]
        rightNode = inOrderNodes[i + 1]
        leftNode.right = rightNode
        rightNode.left = leftNode

    return inOrderNodes[0]

def getNodesInOrder(root, array):
    if root is not None:
        getNodesInOrder(root.left, array)
        array.append(root)
        getNodesInOrder(root.right, array)
    return array

# Optimised approach with leftSubtreeRightMost and rightSubtreeLeftMost approach
# O(n) time | O(d) space
def flattenBinaryTree(root):
    leftMost, rightMost = flattenTree(root)
    return leftMost

def flattenTree(node):
    if node.left is None:
        leftMost = node
    else:
        leftSubtreeLeftMost, leftSubtreeRightMost = flattenTree(node.left)
        connectNodes(leftSubtreeRightMost, node)
        leftMost = leftSubtreeLeftMost

    if node.right is None:
        rightMost = node
    else:
        rightSubtreeLeftMost, rightSubtreeRightMost = flattenTree(node.right)
        connectNodes(node, rightSubtreeLeftMost)
        rightMost = rightSubtreeRightMost
    
    return (leftMost, rightMost)

def connectNodes(left, right):
    left.right = right
    right.left = left