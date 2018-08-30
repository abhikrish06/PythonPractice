class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]

        nums = sorted(nums)

        res = [[nums[0]]]

        for n in nums[1:]:
            rlen = len(res)
            if [n] not in res:
                res.append([n])
            for i in range(rlen):
                if res[i]+[n] not in res:
                    res.append(res[i] + [n])

        res.append([])

        return res

obj = Solution()
print(obj.subsetsWithDup([1,2,2]))