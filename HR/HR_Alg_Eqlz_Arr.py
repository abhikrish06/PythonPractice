#!/bin/python3

import sys
from collections import OrderedDict
def equalizeArray(arr):
    # Complete this function
    d = {}
    for i in arr:
        d[i] = arr.count(i)
    print(d)
    v = list(sorted(d.values()))
    return sum(v[:-1])



if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = equalizeArray(arr)
    print(result)
