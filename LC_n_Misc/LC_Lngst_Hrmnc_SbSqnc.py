class Solution:
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

        # print(d)
        ln = 0

        for i in d:
            if d.get(i + 1):
                ln = max(ln, d[i] + d[i + 1])
        return ln


obj = Solution()
print(obj.findLHS([1,3,2,2,5,2,3,7]))