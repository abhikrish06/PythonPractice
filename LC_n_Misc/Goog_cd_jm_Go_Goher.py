import numpy as np

t = int(input())

for i in range(t):
    a = int(input())
    if a == 20:
        final = False
        while not final:
            x = np.random.randint(9,12)
            y = np.random.randint(10,12)
            print(x,' ',y)
            x1, y1 = map(int, input().split(' '))
            # y1 = int(input())
            if x1 == 0 and y1 == 0:
                final = True
            elif x1 == -1 and y1 == -1:
                final = True
                print('ERROR')
    else:
        final = False
        while not final:
            x = np.random.randint(1, 19)
            y = np.random.randint(1, 9)
            print(x, ' ', y)
            x1, y1 = map(int, input().split(' '))
            # y1 = int(input())
            if x1 == 0 and y1 == 0:
                final = True
            elif x1 == -1 and y1 == -1:
                final = True
                print('ERROR')
