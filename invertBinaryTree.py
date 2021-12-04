class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Iterative solution using List as a Queue
# O(n) time | O(n) space
def invertBinaryTreeIterativeWithList(tree):
    queue = [tree] # Root node
    while len(queue):
        currentNode = queue.pop(0) # O(n) operation in built in List. FIFO order
        if currentNode is None:
            continue
        swapNodes(currentNode) # O(1) time
        queue.append(currentNode.left)
        queue.append(currentNode.right)

def swapNodes(tree):
    tree.left, tree.right = tree.right, tree.left

# Iterative solution using built in Queue. NOT RECOMMENDED
# O(n) time | O(n) space
def invertBinaryTreeIterativeWithQueue(tree):
    from queue import Queue
    q = Queue()
    q.put(tree)

    while q.qsize():
        currentNode = q.get()
        if currentNode is None:
            continue
        swapNodes(currentNode)
        q.put(currentNode.left)
        q.put(currentNode.right)

# Iterative implementation with Deque. O(1) insert delete
# O(n) time | O(n) space
def invertBinaryTreeWithDeque(tree):
    from collections import deque
    dq = deque([tree])

    while len(dq):
        currentNode = dq.popleft() # O(1) time
        if currentNode is None:
            continue
        swapNodes(currentNode)
        dq.append(currentNode.left) # O(1) time
        dq.append(currentNode.right)

# Recursive solution
# O(n) time | O(log(n)) space
def invertBinaryTreeRecursive(tree):
    if tree is None:
        return
    swapNodes(tree)
    invertBinaryTreeRecursive(tree.left)
    invertBinaryTreeRecursive(tree.right)