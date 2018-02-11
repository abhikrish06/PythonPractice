#!/bin/python3

import sys

def countingSort(arr):
    # Complete this function
    print(arr)
    return sorted(arr)

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = countingSort(arr)
    print (" ".join(map(str, result)))