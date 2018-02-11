from collections import OrderedDict

d = OrderedDict()
N = int(input())
for i in range(N):
    lst = list(input().split())
    # print(lst)
    # n = len(lst)
    item, price = ' '.join(lst[:-1]), int(lst[-1])
    if item in d:
        d[item] += price
    else:
        d[item] = price
for k,v in d.items():
    print(k,v)