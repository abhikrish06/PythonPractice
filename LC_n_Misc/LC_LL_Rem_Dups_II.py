# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        else:
            dp_dict = {}
            curr = head
            while curr:
                if curr.val in dp_dict:   # create a dict out of LL
                    dp_dict[curr.val] += 1
                else:
                    dp_dict[curr.val] = 1

            dp_lst = [] # create a list with no duplicate values
            for k,v in dp_dict.items():
                if v > 1:
                    continue
                else:
                    dp_lst.append(k)

            if dp_lst == []:  # create a new LL with dups removed
                return None
            else:
                node1 = ListNode(dp_dict[0])
                head = node1
                for i in dp_lst[1:]:
                    new_node = ListNode(i)
                    node1.next = new_node
                    node1 = new_node

                return head

# another soln within runtime

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        newnode = ListNode(0)
        newnode.next = head
        dup_val = None
        tail = newnode

        while head:
            if head and head.next and head.val == head.next.val:
                dup_val = head.val

            if dup_val == None or head.val != dup_val:
                # add it to the newlist
                tail.next = head
                tail = head

            head = head.next

        tail.next = None
        return newnode.next