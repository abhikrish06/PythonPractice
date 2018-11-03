#!/bin/python3

import sys


def sockMerchant(n, ar):
    # Complete this function
    sock_dict = {}
    cntr = 0
    for i in ar:
        sock_dict[i] = ar.count(i)

    print(sock_dict)

    for v in sock_dict.values():
        if v > 2 or v % 2 == 0:
            cntr = cntr + int(v / 2)
    return cntr


n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = sockMerchant(n, ar)
print(result)
