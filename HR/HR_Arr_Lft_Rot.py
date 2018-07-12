#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the rotLeft function below.
n, d = map(int, input().split())
# print(n,d)
a = list(map(int, input().split()))
# print(n, d, a)

def rotLeft(a, d):
    n = len(a)
    if d%n == 0:
        return a
    dv = d%n
    # print('dv:', dv)
    for i in range(dv):
        val = a.pop(0)
        a.append(val)
        # print(a)

    return a


print(rotLeft(a,d))