# class Solution:
#     def removeDuplicates(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         return len(set(nums))
#
# sol = Solution()
# print(sol.removeDuplicates([1, 1, 2]))
#  # Since the problem is about sorted list, the above is wrong as order is not preserved in set formation
#
# from collections import OrderedDict
# class Solution(object):
#     def removeDuplicates(self, nums):
#
#         nums[:] = OrderedDict.fromkeys(nums) # order is preserved in orderedDict
#         return len(nums)
# 81 : (1,34.3,$23),(2,44.3,$83)
# import sys
# for line in sys.stdin:
#     W, lst = line.split()
# print(W)
# print(lst)
# def rev(s):
#     return int(''.join(s[::-1]))
#
#
# print(rev('20'))
#
# ip = 'append 20    '
# print(ip.rstrip())

# A = [1, 2, 3]
# B = [6, 5, 4]
# C = [7, 8, 9]
# X = [A] + [B] + [C]

# n, x = map(int, input().split())
# lst = []
# for i in range(x):
#     lst.append([map(int, input().split())])
# print(sum(zip(*lst)))



# str = "sa5aS"
# n = len(str)
# ch = ['s', 'S']
# for i in ch:
#     if i in str:
#         str = str.replace(i, '5')
# lst = list(str)
# lst.insert(n//2, 2*)
# print(lst)

from collections import OrderedDict

# target = 1
# nums = [-1, 1, 2, -4]
# nums.sort()
# res = 0
# lst = []
# for i in range(len(nums)-2):
#     print(lst)

from itertools import permutations

# w = 'aab'
# s = 'aabaabaa'
# #print(set(permutations(w)))
# lst = list(s)
# n = len(w)
# i_dict, perm_list = {}, []
# perm_list = list(set(permutations(w)))
# print(perm_list)
# for i in perm_list:
#     for j in range(len(lst)-n):
#         tmp = lst[j:j+n]
#         #print(tmp, i)
#         if tmp == list(i):
#             ky = ''.join(i)
#             if ky in i_dict:
#                 i_dict[ky] += 1
#             else:
#                 i_dict[ky] = 1
#         else:
#             continue
#
# if len(i_dict) == 0:
#     print(-1)
# else:
#     print(list(v[0] for v in sorted(i_dict.items(), key=lambda kv: (-kv[1], kv[0])))[0])

#print(i_dict)

import math

def answer(area):
    ar1 = []
    while area > 0:
        numl = math.sqrt(area)
        nl = math.floor(numl)
        ar1.append(int(nl*nl))
        area -= (nl*nl)
    #print(ar1)

    return ar1

print(answer(15324))