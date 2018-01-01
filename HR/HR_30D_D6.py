t = int(input())
s = []
for i in range(t):
    s.append(input())
for k in range(len(s)):
    str_l = []
    str_2 = []
    l = s[k]
    for j in range(len(l)):
        if j % 2 == 0:
            str_l.append(l[j])
        else:
            str_2.append(l[j])
    print(''.join(str_l), ''.join(str_2))

# one-liner

for i in range(int(input())): s = input(); print(*["".join(s[::2]), "".join(s[1::2])])

# simple soln

for _ in range(int(input())):
    S = input()
    print(''.join(s[::2]), ''.join(s[1::2]))
