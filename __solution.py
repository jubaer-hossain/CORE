# O(n) time | O(n) space
def flattenBinaryTree(root):
    # 1. Traverse the tree inOrder and return the final values in an array
    inOrderNodes = getNodesInOrder(root, []) # Alws pass an empty array when the function needs it.

    # 2. Run a for loop EXCLUDING the LAST NODE because we will be connecting the lastNode when we are at "array(len) - 1" node
    for i in range(0, len(inOrderNodes) - 1):
        leftNode = inOrderNodes[i]
        rightNode = inOrderNodes[i + 1]
        leftNode.right = rightNode
        rightNode.left = leftNode

    # 3. Return the first node
    return inOrderNodes[0]

# Standard inOrder traversal and storing the nodes in an array
def getNodesInOrder(root, array):
    if root is not None:
        getNodesInOrder(root.left, array)
        array.append(root)
        getNodesInOrder(root.right, array)
    return array # We are RETURNING the array MULTIPLE times when we hit the None nodes. But the last/rightMost node's return will overwrite the entire array



# Optimised approach convert a binary tree into a Linked List in-place
# O(n) time | O(d) space
def flattenBinaryTree(root):
    leftMost, rightMost = flattenTree(root)
    return leftMost

def flattenTree(node):
    # 1. Process leftSubtree

    # 1.1. If we're in a leaf node then currentNode is the leftMost
    if node.left is None:
        leftMost = node

    # 1.2. Otherwise get leftSubtree leftMost and RightMost nodes
    else:
        leftSubtreeLeftMost, leftSubtreeRightMost = flattenTree(node.left)

        # 1.3. Connect leftSubtree RightMost with currentNode
        connectNodes(leftSubtreeRightMost, node)

        # 1.4. We need this for parentNodes
        leftMost = leftSubtreeLeftMost


    # 2. Process rightSubtree

    # 2.1 If we're in a leaf node then currentNode is the rightMost
    if node.right is None:
        rightMost = node

    # 2.2. Otherwise get rightSubtree leftMost and RightMost nodes
    else:
        rightSubtreeLeftMost, rightSubtreeRightMost = flattenTree(node.right)

        # 2.3. Connect rightSubtree LeftMost with currentNode
        connectNodes(node, rightSubtreeLeftMost)

        # 1.4. We need this for parentNodes
        rightMost = rightSubtreeRightMost

    # 3. Finally return leftMost and rightMost nodes. Basically leftMost means it is the very leftMost Leaf Node of the currentSubtree.
    return (leftMost, rightMost)

def connectNodes(left, right):
    left.right = right
    right.left = left



    