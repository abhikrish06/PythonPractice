from collections import namedtuple
N, studs, tot = int(input()), namedtuple('studs', input()), 0
# for i in range(N):
#     students = studs(*input().split())
#     tot += int(students.MARKS)
tot = sum([int(i.MARKS) for i in [studs(*input().split()) for _ in range(N)]]) # one-liner equivalent to above for-loop
print('{:.2f}'.format(tot / N))