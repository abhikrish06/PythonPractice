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
def rev(s):
    return int(''.join(s[::-1]))


print(rev('20'))

ip = 'append 20    '
print(ip.rstrip())

# A = [1, 2, 3]
# B = [6, 5, 4]
# C = [7, 8, 9]
# X = [A] + [B] + [C]

n, x = map(int, input().split())
lst = []
for i in range(x):
    lst.append([map(int, input().split())])
print(sum(zip(*lst)))