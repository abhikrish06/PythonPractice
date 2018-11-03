class Solution:
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        i, n = 0, len(nums)
        res = []
        while i < n:
            if nums[i] == i + 1:
                i += 1
                continue

            val = nums[i]
            if val == -1:
                i += 1
                continue

            if nums[val - 1] == val:
                res.append(val)
                nums[val - 1] = -1
                i += 1
                continue
            nums[i], nums[val - 1] = nums[val - 1], nums[i]
        return res

obj = Solution()
print(obj.findDuplicates([4,3,2,7,8,2,3,1]))
