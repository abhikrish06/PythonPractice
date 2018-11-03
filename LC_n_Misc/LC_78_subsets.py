class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]

        res = []
        res.append([nums[0]])
        for i in nums[1:]:
            resL = len(res)
            res.append([i])
            for j in range(resL):
                res.append(res[j] + [i])
        res.append([])

        return res

obj = Solution()
print(obj.subsets([1,2,3]))