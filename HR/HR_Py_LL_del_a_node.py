# https://www.hackerrank.com/challenges/delete-a-node-from-a-linked-list/problem
class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

def Delete(head, position):
    if position == 0:
        head = head.next
    else:
        curr = head
        prev = curr
        for i in range(position):
            prev = curr
            curr = curr.next
        prev.next = curr.next
        curr = curr.next

    return head