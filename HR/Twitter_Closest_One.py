#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the closest function below.
def closest(s, queries):
    dic = {}
    for i in range(len(s)):
        if s[i] in dic:
            dic[s[i]].append(i)
        else:
            dic[s[i]] = [i]
    ans = []
    for q in queries:
        arr = dic[s[q]]
        j = binarysearch(arr, q)
        if j == 0 and j == len(arr) - 1:
            ans.append(-1)
        elif j == 0:
            ans.append(arr[j + 1])
        elif j == len(arr) - 1:
            ans.append(arr[j - 1])
        else:
            if arr[j] - arr[j - 1] <= arr[j + 1] - arr[j]:
                ans.append(arr[j - 1])
            else:
                ans.append(arr[j + 1])
    return ans


def binarysearch(arr, item):
    first = 0
    last = len(arr) - 1
    while (first <= last):
        midpoint = int((first + last) / 2)
        if item == arr[midpoint]:
            return midpoint
        elif item < arr[midpoint]:
            last = midpoint - 1
        else:
            first = midpoint + 1


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    res = closest(s, queries)

    # fptr.write('\n'.join(map(str, res)))
    # fptr.write('\n')
    #
    # fptr.close()

# sample input
# hackerrank
# 4
# 4
# 1
# 6
# 8

# sample output
# -1
# 7
# 5
# -1
