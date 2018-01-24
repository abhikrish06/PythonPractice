t = int(input().strip())
for a0 in range(t):
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    res = []
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            res.append(i & j)
    # print(res)
    print(max([i for i in res if i < k]))

# above soln times out
# below is different n efficient
#
T = int(input().strip())
for _ in range(T):
    n, k = map(int, input().split())
    print(k - 1 if ((k - 1) | k) <= n else k - 2)
