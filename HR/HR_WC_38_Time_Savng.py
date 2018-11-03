# 7
# 4
# 7
# 1 2 3
# 2 3 1
# 1 4 4
# 4 6 7
# 7 5 2
# 3 5 1
# 4 5 5

# lst = [[1, 2, 3], [2, 3, 1], [1, 4, 4], [4, 6, 7], [7, 5, 2], [3, 5, 1], [4, 5, 5]]
# print(len(lst))
# for i in range(7):
#     lst.append(list(map(int, input().split())))


# print(sorted(lst))


# lst = sorted(lst)
# print(lst)
# dct = {lst[0][0]: {lst[0][1]: lst[0][2]}}
#
# for i in range(1, len(lst)):
#     if lst[i][0] in dct:
#         dct[lst[i][0]].update({lst[i][1]: lst[i][2]})
#     else:
#         dct[lst[i][0]] = {lst[i][1]: lst[i][2]}
#
# print(dct)

# !/bin/python3

import math
import os
import random
import re
import sys


# Complete the leastTimeToInterview function below.
def leastTimeToInterview(n, k, lst):
    # Return the least amount of time needed to reach the interview location in seconds.
    lst = sorted(lst)
    print(lst)
    dct = {lst[0][0]: {lst[0][1]: lst[0][2]}}

    for i in range(1, len(lst)):
        if lst[i][0] in dct:
            dct[lst[i][0]].update({lst[i][1]: lst[i][2]})
        else:
            dct[lst[i][0]] = {lst[i][1]: lst[i][2]}

    start, goal = 1, n
    shrtst_dst = {}
    not_visited = dct
    inf = 9999999

    for node in not_visited:
        shrtst_dst[node] = inf
    shrtst_dst[start] = 0

    while not_visited:
        minNode = None
        for node in not_visited:
            if minNode is None:
                minNode = None
            elif shrtst_dst[node] < shrtst_dst[minNode]:
                minNode = node

        for ngbhr, wt in dct[minNode].items():
            if wt + shrtst_dst[minNode] < shrtst_dst[ngbhr]:
                shrtst_dst[ngbhr] = wt + shrtst_dst[minNode]
        not_visited.pop(minNode)


    return lst


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    k = int(input())

    m = int(input())

    list_m = []

    for i in range(m):
        list_m.append(list(map(int, str(m).split())))

    result = leastTimeToInterview(n, k, list_m)

    fptr.write(str(result) + '\n')

    fptr.close()
