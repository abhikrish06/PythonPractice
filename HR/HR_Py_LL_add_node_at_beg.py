# Insert a node at the head of a linked list
# https://www.hackerrank.com/challenges/insert-a-node-at-the-head-of-a-linked-list/problem

class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

def Insert(head, data):
    nw_node = Node(data,None)
    if head is None:
        return(nw_node)
    else:
        nw_node.next = head
        head = nw_node
    return head