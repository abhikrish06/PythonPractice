# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        curr = head
        while(head):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

####
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # prev = None
        # curr = head
        # while(head):
        #     nxt = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = nxt
        # return prev
        if head == None:
            return None
        elif head != None and head.next == None:
            return head
        else:
            temp = None
            # next_node = None
            while head != None:
                next_node = head.next
                head.next = temp
                temp = head
                head = next_node
            return temp