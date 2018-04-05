#!/bin/python3

import sys

if __name__ == "__main__":
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    # arr_n = [0 for i in range(n+1)]
    # print(arr_n)
    dict_abk = {}
    for a0 in range(m):
        a, b, k = input().strip().split(' ')
        a, b, k = [int(a), int(b), int(k)]

        if a in dict_abk:
            dict_abk[a] += k
        else:
            dict_abk[a] = k

        if b in dict_abk:
            dict_abk[b] += k
        else:
            dict_abk[b] = k
        print(dict_abk)

    print(max(dict_abk.values()))

# 5 3
# 1 2 100
# 2 5 100
# 3 4 100


# if __name__ == "__main__":
#     n, m = [int(n) for n in input().split()]
#     l = [0]*(n+1)
#     for _ in range(m):
#         a, b, k = [int(n) for n in input().split()]
#         l[a-1] += k
#         l[b] -= k
#         print(l)
#     max = a = 0
#     for i in l:
#        a+=i
#        if max<a:
#             max=a
#     print(max)