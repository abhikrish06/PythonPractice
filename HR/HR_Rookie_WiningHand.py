#!/bin/python3

import sys
from itertools import permutations

def winningHands(m, x, a):
    # Complete this function
    srt_a = sorted(a)
    for i in range(1, len(a)+1):
        lst = list(permutations(a, i))
        print(lst)

if __name__ == "__main__":
    n, m, x = input().strip().split(' ')
    n, m, x = [int(n), int(m), int(x)]
    a = list(map(int, input().strip().split(' ')))
    result = winningHands(m, x, a)
    print(result)

# incomplete
