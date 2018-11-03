#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

for i in range(len(arr)-1, -1, -1):
    print(arr[i], end=' ')

# one-liners
print(" ".join(map(str, arr[::-1])))

#another
print(' '.join(map(str, reversed(arr))))

# yet another
print(*reversed(arr))