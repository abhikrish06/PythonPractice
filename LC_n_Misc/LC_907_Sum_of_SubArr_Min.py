# TLE
import sys


class Solution:
    def sumSubarrayMins(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        res = []

        def sub_lists(list1):

            # store all the sublists
            sublist = [[]]

            # first loop
            for i in range(len(list1) + 1):

                # second loop
                for j in range(i + 1, len(list1) + 1):
                    # slice the subarray
                    sub = list1[i:j]
                    res.append(min(sub))
                    sublist.append(sub)
            print(sublist)
            return sum(res)

        sm = sub_lists(A)
        if sm >= sys.maxsize:
            return sm % (10 ** 9 + 7)
        else:
            return sm

obj = Solution()
print(obj.sumSubarrayMins([3,1,2,4]))
# [[], [1], [1, 2], [1, 2, 3], [1, 2, 3, 4], [2], [2, 3], [2, 3, 4], [3], [3, 4], [4]]
# [[], [3], [3, 1], [3, 1, 2], [3, 1, 2, 4], [1], [1, 2], [1, 2, 4], [2], [2, 4], [4]]
