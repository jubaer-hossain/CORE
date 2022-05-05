# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
        
# O(n) time | O(n) space
def copyRandomList(self, head):
    """
    :type head: Node
    :rtype: Node
    """
    oldListCopyHashMap = {None: None} # If any Node's random pointer points to None then in the copied list it should also point to None. Otherwise It will return a Key error that no None value is present in the map

    currentNode = head
    while currentNode:
        copy = Node(currentNode.val) # The only mistake is here. We need to create a new Node object
        oldListCopyHashMap[currentNode] = copy
        currentNode = currentNode.next

    currentNode = head
    while currentNode:
        copiedNode = oldListCopyHashMap[currentNode]
        copiedNode.next = oldListCopyHashMap[currentNode.next]
        copiedNode.random = oldListCopyHashMap[currentNode.random]
        currentNode = currentNode.next

    return oldListCopyHashMap[head]


