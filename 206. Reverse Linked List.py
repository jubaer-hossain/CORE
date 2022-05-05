"""
3 Steps for recursion:
1. Get new head from the next recursive call
2. Reverse/Change connection of the current Node
3. In current call, head.next should be None cause we are only dealind with the current portion of the linked list
4. Return the newHead to previous node
"""

# O(n) time | O(n) space cause of recursion
class Solution(object):
    def reverseList(self, head):
        # Base case
        if head is None:
            return None

        newHead = head
        if head.next is not None: # We need to get the new head from next
            newHead = self.reverseList(head.next)
            
            # Reversing the connection
            nextNode = head.next
            nextNode.next = head # 1 - 2 - 3 - None. So if head is 2 then we are changing 2.next which is 3 and it's next value to 2
        
        head.next = None # We are daeling with the current segment of the list. So the current head should be set to None since it is the end of the list now after reversing
        return newHead


        