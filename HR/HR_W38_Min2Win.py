#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import zip_longest

# Complete the minuteToWinIt function below.
def minuteToWinIt(a, k):
    # Return the minimum amount of time in minutes.
    lst = [a[0]+k*i for i in range(len(a))]
    cntr = 0
    for (x,y) in zip_longest(lst,a):
        if x != y:
            cntr += 1
    return cntr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    a = list(map(int, input().rstrip().split()))

    result = minuteToWinIt(a, k)

    fptr.write(str(result) + '\n')

    fptr.close()
