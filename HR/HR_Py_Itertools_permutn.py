from itertools import permutations
s, k = input().split()
slst = list(sorted(s))

all_perms = list(permutations(slst, int(k)))

for i in range(len(all_perms)):
    print(''.join(all_perms[i]))

# One liner
print(*[''.join(i) for i in permutations(sorted(s),int(k))],sep='\n')