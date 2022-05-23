def compareLeafTraversal(tree1, tree2):
    stack1 = [tree1]
    stack2 = [tree2]

    while len(stack1) > 0 and len(stack2) > 0:
        leaf1 = getLeaf(stack1)
        leaf2 = getLeaf(stack2)

        if leaf1.value != leaf2.value:
            return False

    return len(stack1) == 0 and len(stack2) == 0

# Pre-order DFS traversal
def getLeaf(stack):
    currentNode = stack.pop()

    while not isLeaf(currentNode):
        if currentNode.right is not None:
            stack.append(currentNode.right)

        if currentNode.left is not None:
            stack.append(currentNode.left)

        currentNode = stack.pop()


    return currentNode

def isLeaf(node):
    return node.left is None and node.right is None



def compareLeafTraversal(tree1, tree2):
    # 1. Create two linked list. These are the heads of the lists
    list1, _ = createList(tree1)
    list2, _ = createList(tree2)

    # 2. Traverse through the list and compare each node's value 
    while list1 is not None and list2 is not None:
        if list1.value != list2.value:
            return False
        list1 = list1.right
        list2 = list2.right

    return list1 is None and list2 is None

def createList(currentNode, head = None, previous = None):
    # 0. Base case: When the node is None we return upward the head and previous
    if currentNode is None:
        return head, previous

    # 1.1. When node is a Leaf node: We need to connect the node with previous
    if isLeaf(currentNode):
        # 1.2. If this is the leftMost leaf
        if head is None:
            head = currentNode
            previous = currentNode
        else:
            previous.right = currentNode

        # 1.3. Update the previous node to currentNode for the next recursive call
        previous = currentNode

    # 2. Call left & right subtree to get their head & previous nodes
    leftSubtreeHead, leftSubtreePrevious = createList(currentNode.left, head, previous)

    # 3. Call right subtree with the leftSubtree head and previous to connect them with right subtree
    return createList(currentNode.right, leftSubtreeHead, leftSubtreePrevious)

