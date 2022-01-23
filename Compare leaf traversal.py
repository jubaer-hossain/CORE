class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# O(n + m) time | O(h1 + h2) space
def compareLeafTraversal(tree1, tree2):
    tree1TraversalStack = [tree1]
    tree2TraversalStack = [tree2]

    while len(tree1TraversalStack) > 0 and len(tree2TraversalStack) > 0:
        tree1Leaf = getNextLeafNode(tree1TraversalStack)
        tree2Leaf = getNextLeafNode(tree2TraversalStack)

        if tree1Leaf.value != tree2Leaf.value:
            return False
    
    return len(tree1TraversalStack) == 0 and len(tree2TraversalStack) == 0

def getNextLeafNode(traversalStack):
    currentNode = traversalStack.pop() # Last element

    while not isLeafNode(currentNode):
        if currentNode.right is not None:
            traversalStack.append(currentNode.right)
        
        if currentNode.left is not None:
            traversalStack.append(currentNode.left)
        
        currentNode = traversalStack.pop()
    
    return currentNode

def isLeafNode(node):
    return node.left is None and node.right is None



# Linked List approach
# O(n + m) time | O(max(h1, h2)) space
def compareLeafTraversal(tree1, tree2):
    tree1LeafNodesLinkedList, _ = connectLeafNodes(tree1)
    tree2LeadNodesLinkedList, _ = connectLeafNodes(tree2)
    
    list1CurrentNode = tree1LeafNodesLinkedList
    list2CurrentNode = tree2LeadNodesLinkedList

    while list1CurrentNode is not None and list2CurrentNode is not None:
        if list1CurrentNode.value != list2CurrentNode:
            return False
        
        list1CurrentNode = list1CurrentNode.right
        list2CurrentNode = list2CurrentNode.right
    
    return list1CurrentNode is None and list2CurrentNode is None

def connectLeafNodes(currentNode, head = None, previousNode = None):
    if currentNode is None: # None node base case: return
        return head, previousNode
    
    if isLeafNode(currentNode): # Leaf node base case: calculate linked list
        if previousNode is None:
            head = currentNode
        else:
            previousNode.right = currentNode
        
        previousNode = currentNode
    
    leftHead, leftPreviousNode = connectLeafNodes(currentNode.left, head, previousNode)
    return connectLeafNodes(currentNode.right, leftHead, leftPreviousNode)

def isChildNode(node):
    return node.left is None and node.right is None