#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort1 function below.
def insertionSort1(n, arr):
    val = arr[-1]
    i = n - 2
    while val < arr[i] and n>=0:
        arr[i+1] = arr[i]
        i -= 1
        print(print(' '.join(map(str,arr))))

    arr[i+1] = val
    print(' '.join(map(str,arr)))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)


