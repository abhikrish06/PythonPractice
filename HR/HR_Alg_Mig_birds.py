#!/bin/python3

import sys
from collections import OrderedDict


def migratoryBirds(n, ar):
    # Complete this function
    cnt_lst = [0]*n
    for i in ar:
        cnt_lst[i] += 1
    return cnt_lst.index(max(cnt_lst))

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = migratoryBirds(n, ar)
print(result)
