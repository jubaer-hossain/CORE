# O(n) time | O(1) space
def rotateList(self, head, k):
    # Edge case: Empty linked list
    if head is None:
        return head

    # Calculate the length of the linked list
    linkedListLength = 1 # Because the first node Head is already 1 node
    tail = head
    while tail.next is not None:
        tail = tail.next # Pushing the counter to left
        linkedListLength += 1
    
    k = k % linkedListLength # Rounding down the K value if it's larget than the list length
    
    # Edge case: If k == 0 then we don't need to rotate anything
    if k == 0:
        return head
    
    # Move to pivot position
    placesToShift = (linkedListLength - k - 1) # -1 because we are SHIFTING 2 position
    
    currentNode = head
    for i in range(placesToShift):
        currentNode = currentNode.next
    
    newHead = currentNode.next # Setting the new head
    currentNode.next = None # We are at the pivot point. So the next of currentNode will be none after rotating
    tail.next = head # Connecting the last part of the list to previous head

    return newHead


