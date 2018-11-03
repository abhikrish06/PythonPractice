import re
n = int(input())
for i in range(n):
    s = input().strip()
    print(bool(re.match(r'^[-+]?[0-9]*\.[0-9]+$', s)))
