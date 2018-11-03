# Write code to remove duplicates from an unsorted linked list.

class Node():
    def __init__(self, data, next):
        self.data = data
        self.next = next


def removeDups(head):
    node = head
    if node:
        values = {node.data: True}
        while node.next:
            if node.next.data in values:
                node.next = node.next.next
            else:
                values[node.next.data] = True
                node = node.next
    return head


import unittest


class Test(unittest.TestCase):
    def test_remove_duplicates(self):
        # head = Node(1, Node(3, Node(3, Node(1, Node(5, None)))))
        head = Node('F',Node('O',Node('L',Node('L',Node('O',Node('W',None))))))
        removeDups(head)
        self.assertEqual(head.data, 'F')
        self.assertEqual(head.next.data, 'O')
        self.assertEqual(head.next.next.data, 'L')
        self.assertEqual(head.next.next.next.data, 'W')
        self.assertEqual(head.next.next.next.next, None)
        # self.assertEqual(head.data, 1)
        # self.assertEqual(head.next.data, 3)
        # self.assertEqual(head.next.next.data, 5)
        # self.assertEqual(head.next.next.next, None)


if __name__ == "__main__":
    unittest.main()
