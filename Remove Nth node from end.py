# O(n) time | O(1) space
def removeNthNodeFromEnd(head, n):
    # Shifting second node FORWARD by n
    counter = 1
    first = head
    second = head

    # F                   S
    # O -> 1 -> 2 -> 3 -> 4 -> None
    # Here watch that we use <= n because we want our second node to be n node AHEAD of the first
    while counter <= n:
        second = second.next
        counter += 1
    
    # Edge case: if the node to remove is the head
    if second is None: 
        head.value = head.next.value # Update head's value
        head.next = head.next.next # Update head's next pointer to the 3rd node in the original list
        return

    # Traversing the list in sliding window
    # first is pointing to the node node right before the node we want to remove
    # first.next = NODE_TO_REMOVE
    # first.next = NODE_TO_REMOVE.next
    while second.next is not None:
        first = first.next
        second = second.next
    
    first.next = first.next.next


