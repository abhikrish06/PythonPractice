# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None

        ptA = headA
        ptB = headB

        while ptA is not ptB:
            if ptA is None:
                ptA = headB
            else:
                ptA = ptA.next

            if ptB is None:
                ptB = headA
            else:
                ptB = ptB.next
        return ptB # or ptA