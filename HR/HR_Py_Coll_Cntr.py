from collections import Counter
X = int(input())
shoe_sizes = Counter(map(int, input().split()))
N = int(input())
arr = []
for i in range(N):
    arr_demand = [int(a) for a in input().split()]
    arr.append(arr_demand)

earn = 0
for i in arr:
    size = i[0]
    if shoe_sizes[size]:
        earn += i[1]
        shoe_sizes[size] -= 1

# print(shoe_sizes)
# print(arr)
print(earn)

# similar but simpler one
import collections
numShoes = int(input())
shoes = collections.Counter(map(int, input().split()))
numCust = int(input())
income = 0
for i in range(numCust):
    size, price = map(int, input().split())
    if shoes[size]:
        income += price
        shoes[size] -= 1
print(income)