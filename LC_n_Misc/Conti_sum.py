# def answer(l, t):
#     res, val_lst = [], []
#     t_cur = t
#     if len(l) == 1 and l[0] == t:
#         val_lst.append(l[0])
#         res.append(0)
#     elif len(l) == 1 and l[0] != t:
#         res = [-1, -1]
#     else:
#         i = 0
#         while i < len(l):
#             if l[i] == t_cur:
#                 val_lst.append(l[i])
#                 res.append(i)
#                 break
#             elif l[i] < t_cur:
#                 val_lst.append(l[i])
#                 res.append(i)
#                 t_cur = t_cur - l[i]
#                 i += 1
#             elif l[i] > t_cur:
#                 res = []
#                 val_lst = []
#                 t_cur = t
#                 # i = i - 1
#
#     if len(res) >= 0 and sum(val_lst) == t:
#         return res
#     else:
#         return [-1, -1]


# def answer(l, t):
#     curr_sum = l[0]
#     start = 0
#
#     i = 1
#     while i <= len(l):
#         while curr_sum > t and start < i - 1:
#             curr_sum = curr_sum - l[start]
#             start += 1
#             if curr_sum == t:
#                 return [start, i-1]
#
#         if i < len(l):
#             curr_sum = curr_sum + l[i]
#         i += 1
#
#     return [-1, -1]


def answer(l, t):
    n = len(l)
    for i in range(n):
        t_curr = l[i]

        j = i + 1
        while j <= n:

            if t_curr == t:
                return [i, j - 1]
            if t_curr > t or j == n:
                break

            t_curr = t_curr + l[j]
            j += 1

    return [-1, -1]


print(answer([4, 3, 10, 2, 8], 12))
print(answer([12], 12))
print(answer([1, 2, 3, 4], 12))
print(answer([10], 12))
print(answer([1, 4, 20, 3, 10, 5], 33))
