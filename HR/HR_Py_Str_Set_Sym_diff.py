m = int(input())
M = set(map(int, input().split()))
n = int(input())
N = set(map(int, input().split()))

sym_diff = sorted((M.difference(N)).union(N.difference(M)))

for i in sym_diff:
    print(i)
