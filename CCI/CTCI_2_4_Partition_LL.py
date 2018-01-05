# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head == None:
            return head

        p1Head = None
        p1Tail = None
        p2Head = None
        p2Tail = None

        curr = head

        while curr:
            if (curr.val < x):
                if p1Head == None:
                    p1Head = curr
                    p1Tail = curr
                else:
                    p1Tail.next = curr
                    p1Tail = curr
            else:
                if p2Head == None:
                    p2Head = curr
                    p2Tail = curr
                else:
                    p2Tail.next = curr
                    p2Tail = curr

            curr = curr.next

        if p1Head == None:
            return p2Head

        if p2Head == None:
            return p1Head

        p1Tail.next = p2Head
        p2Tail.next = None
        return p1Head