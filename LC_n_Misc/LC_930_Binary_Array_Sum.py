import collections


class Solution:
    def numSubarraysWithSum(self, A, S):
        """
        :type A: List[int]
        :type S: int
        :rtype: int
        """
        curr, res = 0, 0
        dct = collections.defaultdict(int)
        print(dct)
        for b in A:
            dct[curr + S] += 1
            # print(dct)
            curr += b
            res += dct[curr]
            print(dct)
        return res


obj = Solution()
print(obj.numSubarraysWithSum([1, 0, 1, 0, 1], 2))
