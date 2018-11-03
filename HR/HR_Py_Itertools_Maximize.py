from itertools import product

K, M = map(int, input().split())
lol = []
for i in range(K):
    lol.append([int(x) for x in input().split()][1:])
# print(lol)

poss_com = list(product(*lol))


def calSum(nums):
    return sum(x * x for x in nums) % M


print(max(list(map(calSum, poss_com))))
