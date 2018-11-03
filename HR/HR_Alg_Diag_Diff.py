#!/bin/python3

import sys


def diagonalDifference(a):
    # Complete this function
    l = len(a)
    sum_diag1, sum_diag2 = 0, 0
    for i in range(l):
        sum_diag1 += a[i][i]
        sum_diag2 += a[n-i-1][i]
    return abs(sum_diag1 - sum_diag2)

# n = int(input().strip())
# dSumLeft  = 0
# dSumRight  = 0
# for i in range(n):
#     matrixRow = list(map(int,input().strip().split(' ')))
#     dSumLeft += int(matrixRow[i])
#     dSumRight += int(matrixRow[n-i-1])
# print(abs(dSumLeft - dSumRight))

if __name__ == "__main__":
    n = int(input().strip())
    a = []
    for a_i in range(n):
        a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
        a.append(a_t)
    print(a)
    result = diagonalDifference(a)
    print(result)
