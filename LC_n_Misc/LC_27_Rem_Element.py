class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums: return 0
        n = len(nums)-1

        while n >= 0:
            if nums[n] == val:
                nums.pop(n)
            n -= 1
            #print(nums)
        return len(nums)

obj = Solution()
print(obj.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))
