# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node = head
        if node:
            values = {node.val: True}
            while node.next:
                if node.next.val in values:
                    node.next = node.next.next
                else:
                    values[node.next.val] = True
                    node = node.next
        return head