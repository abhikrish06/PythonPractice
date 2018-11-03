# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if (l1 == None and l2 == None):
            return None
        elif (l1 == None and l2 != None):
            return l2
        elif (l1 != None and l2 == None):
            return l1
        else:
            p = ListNode(0)
            dummy = p
            while(l1 != None and l2 != None):
                if (l1.val < l2.val):
                    p.next = l1
                    l1 = l1.next
                else:
                    p.next = l2
                    l2 = l2.next
                p = p.next
        if l1 != None:
            p.next = l1

        if l2 != None:
            p.next = l2

        return dummy.next
