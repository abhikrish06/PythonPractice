# Insert a node at a specific position in a linked list
# https://www.hackerrank.com/challenges/insert-a-node-at-a-specific-position-in-a-linked-list/problem

class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

def InsertNth(head, data, position):
    nw_node = Node(data, None)
    if position == 0:
        if head is None:
            return(nw_node)
        else:
            nw_node.next = head
            head = nw_node
    else:
        curr = head
        for i in range(position):
            prev = curr
            curr = curr.next
        prev.next = nw_node
        nw_node.next = curr
    return head