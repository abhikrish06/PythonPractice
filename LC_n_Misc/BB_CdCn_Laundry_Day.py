import sys

d = {}
data = [input().splitlines()]
for line in data:
    print(line)
    if line[0] in d:
        d[line[0]] += 1
    else:
        d[line[0]] = 1
        # print(d)
for k, v in d.items():
    if 'sock' in k:
        if v > 2 and v % 2 == 1:
            print(str(v / 2)+'|'+ k)
            print('0|', k)
    else:
        print(str(v)+'|'+str(k))
