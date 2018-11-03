from collections import deque
d = deque()
for i in range(int(input())):
    cmd = input().rstrip()
    if 'popleft' in cmd:
        d.popleft()
    elif 'pop' in cmd:
        d.pop()
    else:
        cmd2, val = cmd.split(' ')
        if 'appendleft' in cmd2:
            d.appendleft(val)
        elif 'append' in cmd2:
            d.append(val)

print(*[i for i in d])

# Alt. soln
from collections import deque
d = deque()
for i in range(int(input())):
    inp = input().split()
    getattr(d, inp[0])(*[inp[1]] if len(inp) > 1 else [])
    # the above line is equivalent to
    # if len(inp) > 1:
    #     getattr(d, inp[0])(inp[1])
    # else:
    #     getattr(d, inp[0])
print(*[i for i in d])