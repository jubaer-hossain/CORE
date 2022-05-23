# O(n) time | O(1) space
def reverseList(self, head):
    previoudNode, currentNode = None, head

    while currentNode is not None:
        nextNode = currentNode.next # Storing the next node before we break the link

        currentNode.next = previoudNode
        previoudNode = currentNode
        currentNode = nextNode

    return previoudNode


