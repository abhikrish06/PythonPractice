# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def str_to_linked(self, s): # making a linked list out of a string
        linklst = ListNode(s[0])
        if len(s) == 1:
            return linklst
        else:
            linklst.next = self.str_to_linked(s[1:])
        return linklst

# taking space separated input and forming list of list
    arr = []
    for arr_i in range(int(input())):
        arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
        arr.append(arr_t)

# fractions in use (https://www.hackerrank.com/challenges/reduce-function/problem)
from fractions import Fraction
if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)