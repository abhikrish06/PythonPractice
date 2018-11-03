from collections import OrderedDict
d = OrderedDict()
for i in range(int(input())):
    obj = input().strip()
    if obj in d:
        d[obj] += 1
    else:
        d[obj] = 1
print(len(d))
print(*d.values())

# new way of taking counter of OrderedDict items
from collections import Counter, OrderedDict
class OrderedCounter(Counter, OrderedDict):
    pass
d = OrderedCounter(input() for _ in range(int(input())))
print(len(d))
print(*d.values())