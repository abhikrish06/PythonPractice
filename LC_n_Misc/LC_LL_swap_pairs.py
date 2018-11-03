# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr = head
        while curr and curr.next:
            temp = curr.val
            curr.val = curr.next.val
            curr.next.val = temp

            curr = curr.next
            curr.next = curr.next.next
        return head