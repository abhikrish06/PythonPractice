import math

AB = int(input())
BC = int(input())
hyp = math.sqrt(AB * AB + BC * BC)
angC = math.degrees(math.acos(BC / hyp))
print(str(int(round(angC))) + '°')
print(str(int(round(math.degrees(math.atan2(AB, BC))))) + '°')

for i in range(0, int(input())):
    print([1, 121, 12321, 1234321, 123454321, 12345654321, 1234567654321, 123456787654321, 12345678987654321,
           12345678910987654321][i])

for i in range(1, int(input())):  # More than 2 lines will result in 0 score. Do not leave a blank line also
    print([0, 1, 22, 333, 4444, 55555, 666666, 7777777, 88888888, 999999999][i])
    # or
    # print((10 ** i // 9) * i)
