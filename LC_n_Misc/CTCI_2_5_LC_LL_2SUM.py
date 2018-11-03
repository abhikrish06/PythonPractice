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

        while(node1 or node2 or carry):
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

#FOLLOW UP

