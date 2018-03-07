#!/bin/python3

import os
import sys


# Complete the function below.

def heightAndTotalHeight(arr):
    # Write your code here.
    root = arr[0]
    lft, ryt, res = [], [], []
    for i in range(1,len(arr)):
        if arr[i] < root:
            lft.append(arr[i])
        else:
            ryt.append(arr[i])
    res.append(len(lft) + len(ryt))

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    arr_size = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = heightAndTotalHeight(arr)

    f.write("\n".join(map(str, result)))

    f.write('\n')

    f.close()
