from itertools import product

a = list(map(int, input().split()))
b = list(map(int, input().split()))

for i in a:
    for j in b:
        print((i, j), end=" ")
print("")
# using itertools
print(*product(a, b))