# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        node1, node2 = l1, l2
        carry = 0
        res_head, res_node = None, None

        while node1 or node2 or carry:
            value = carry
            if node1:
                value += node1.val
                node1 = node1.next
            if node2:
                value += node2.val
                node2 = node2.next
            if res_node:
                res_node.next = ListNode(value % 10)
                res_node = res_node.next
            else:
                res_node = ListNode(value % 10)
                res_head = res_node
            carry = value / 10
        return res_head

# Alternate better soln
#     def addTwoNumbers(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
#         s1 = ''
#         while l1 != None:
#             s1 += str(l1.val)
#             l1 = l1.next
#         s1 = s1[::-1]
#         s2 = ''
#         while l2 != None:
#             s2 += str(l2.val)
#             l2 = l2.next
#         s2 = s2[::-1]
#         s = str(int(s1) + int(s2))[::-1]
#         return self.str_to_linked(s)
#
#     def str_to_linked(self, s):
#         l = ListNode(s[0])
#         if len(s) == 1:
#             return l
#         else:
#             l.next = self.str_to_linked(s[1:])
#         return l
