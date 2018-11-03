from itertools import combinations

n = int(input())
ip_str = list(input().split())
k = int(input())

tple = tuple(combinations(ip_str, k))
print(tple)
f = []

for i in tple:
    if 'a' in i:
        f.append(i)

print(len(f)/len(tple))
