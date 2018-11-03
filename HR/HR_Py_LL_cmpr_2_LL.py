"""
 Merge two linked list
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""


def CompareLists(headA, headB):
    lstA, lstB = [], []
    cntr = 0
    while (headA):
        lstA.append(headA.data)
        headA = headA.next
    while (headB):
        lstB.append(headB.data)
        headB = headB.next
    if len(lstA) != len(lstB):
        return 0
    else:
        for i in range(len(lstA)):
            if lstA[i] == lstB[i]:
                cntr += 1
        if cntr == len(lstA):
            return 1
        else:
            return 0


# simpler soln
def CompareLists(headA, headB):
    while headA or headB:
        if not (headA and headB) or headA.data != headB.data:
            return 0
        headA = headA.next
        headB = headB.next
    return 1
