from collections import deque

for _ in range(int(input())):
    _, d = int(input()), deque(map(int, input().split()))
    res = 'Yes'
    if max(d) not in (d[0], d[-1]):
        res = 'No'
    print(res)