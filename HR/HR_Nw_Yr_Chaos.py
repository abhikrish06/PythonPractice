#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the minimumBribes function below.
def minimumBribes(q):
    for k, v in enumerate(q):
        if abs(k - (v - 1)) > 2:
            return "Too chaotic"

    n = len(q)
    cntr = 0
    for i in range(n - 1, 0, -1):
        for j in range(i):
            if q[j] > q[j + 1]:
                q[j], q[j + 1] = q[j + 1], q[j]
                cntr += 1
                val = True
        if val:
            val = False
        else:
            break
    return cntr


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)

# 2
# 5
# 2 1 5 3 4
# 5
# 2 5 1 3 4
