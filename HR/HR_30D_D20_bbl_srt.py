#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
cntr_tot = 0
for i in range(n):
    cntr = 0
    for j in range(0, n - 1, 1):
        print('before: ', a)
        if a[j] > a[j + 1]:
            temp = a[j]
            a[j] = a[j + 1]
            a[j + 1] = temp
            cntr += 1
        print('after: ', a)
    if cntr == 0:
        break
    print(cntr)
    cntr_tot = cntr_tot + cntr
    print(cntr_tot)
print('Array is sorted in', cntr_tot, 'swaps.')
print('First Element:', a[0])
print('Last Element:', a[-1])
