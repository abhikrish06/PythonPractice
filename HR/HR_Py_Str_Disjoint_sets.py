# Disjoint Set
n, m = input().split()
N = list(input().split())
A = set(input().split())
B = set(input().split())
# print(sum([(i in A) - (i in B) for i in N]))

hCount = 0
for i in N:
    if i in A:
        hCount += 1
    elif i in B:
        hCount += -1
print(hCount)

# .add() function in set
N = int(input())
stmp = set()
for i in range(N):
    stmp.add(input())

print(len(stmp))