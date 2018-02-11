#!/bin/python3

import math

def viralAdvertising(n):
    # Complete this function
    i = 5
    stk = []
    for j in range(0,n):
        val = math.floor(i/2)
        stk.append(val)
        i = val*3
    return sum(stk)

if __name__ == "__main__":
    n = int(input().strip())
    result = viralAdvertising(n)
    print(result)
