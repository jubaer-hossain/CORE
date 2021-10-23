# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def swapPairs(self, head: ListNode) -> ListNode:
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # If the list has no node or has only one node left.
        if not head or not head.next:
            return head

        # Nodes to be swapped
        first_node = head
        second_node = head.next

        # Swapping
        first_node.next  = self.swapPairs(second_node.next) # For any iteration, First node will be second node after swapping and the next node of first node will be swapped version of the next two pairs of node. Or in other words, what ever Node the next recursive call returns to the first Node 
        second_node.next = first_node

        # Now the head is the second node
        return second_node


'''My algoexpert solution'''

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def nodeSwap(head):
	if head is None or head.next is None:
		return head
	
	# Two nodes that we want to swap
	first_node = head
	second_node = head.next
	
	# Swapping
	first_node.next = nodeSwap(first_node.next.next) # Or can use second_node.next. Both are same
	second_node.next = first_node
	return second_node
