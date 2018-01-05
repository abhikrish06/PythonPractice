import unittest

class Node():
  def __init__(self, data, next=None):
    self.data = data
    self.next = next

def kthNodeFrmLast(head, k):
    if head is None or k < 1:
        return None
    leader = head
    follower = head

    for i in range(k):
        if leader is None:
            return None
        leader = leader.next

    while leader is not None:
        leader = leader.next
        follower = follower.next

    return follower

class Test(unittest.TestCase):
  def test_kth_to_last(self):
    head = Node(1,Node(2,Node(3,Node(4,Node(5,Node(6,Node(7)))))))
    self.assertEqual(None, kthNodeFrmLast(head, 0));
    self.assertEqual(7, kthNodeFrmLast(head, 1).data);
    self.assertEqual(4, kthNodeFrmLast(head, 4).data);
    self.assertEqual(2, kthNodeFrmLast(head, 6).data);
    self.assertEqual(1, kthNodeFrmLast(head, 7).data);
    self.assertEqual(None, kthNodeFrmLast(head, 8));

if __name__ == "__main__":
  unittest.main()