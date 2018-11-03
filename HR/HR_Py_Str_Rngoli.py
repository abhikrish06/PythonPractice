# import string
#
# def print_rangoli(size):
#     letter_dict = {}
#     for i in range(size):
#         letter_dict[i + 1] = string.ascii_lowercase[i]
#     print(letter_dict)
#     for i in range(size, 1, -2):
#         for j in range():
#         print(("-" * size) + letter_dict[i] + ("-" * size))
#
# print_rangoli(3)

import string
alpha = string.ascii_lowercase

n = int(input())
L = []
for i in range(n):
    s = "-".join(alpha[i:n])
    L.append((s[::-1]+s[1:]).center(4*n-3, "-"))
print('\n'.join(L[:0:-1]+L))
