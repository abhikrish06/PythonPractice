# Insert a Node at the Tail of a Linked List
# https://www.hackerrank.com/challenges/insert-a-node-at-the-tail-of-a-linked-list/problem

class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

def Insert(head, data):
    if head == None:
        return Node(data, None)
    nw_node = Node(data, None)
    curr = head
    while curr.next is not None:
        curr = curr.next
    curr.next = nw_node
    return head