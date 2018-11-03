#!/bin/python3

import sys

def getMoneySpent(keyboards, drives, s):
    # Complete this function
    key_sort = sorted(keyboards)
    USB_sort = sorted(drives)
    if s < key_sort[0] + USB_sort[0]:
        return -1
    else:
        max_exp = 0
        for i in key_sort:
            for j in USB_sort:
                val = i + j
                if val < s:
                    if val > max_exp:
                        max_exp = val
        return max_exp

s,n,m = input().strip().split(' ')
s,n,m = [int(s),int(n),int(m)]
keyboards = list(map(int, input().strip().split(' ')))
drives = list(map(int, input().strip().split(' ')))
#  The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
moneySpent = getMoneySpent(keyboards, drives, s)
print(moneySpent)
