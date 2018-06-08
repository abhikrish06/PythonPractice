class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for val in nums:
            if val == target:
                return nums.index(val)

        for val in nums:
            if val > target:
                return nums.index(val)
        return len(nums)

    def searchInsert2(self, nums, target):
        lo, hi = 0, len(nums)-1

        while lo <= hi:
            mid = (lo+hi)//2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        return hi+1


obj = Solution()
print(obj.searchInsert([1, 3, 5, 6], 5))
print(obj.searchInsert([1, 3, 5, 6], 2))
print(obj.searchInsert([1, 3, 5, 6], 7))
print(obj.searchInsert([1, 3, 5, 6], 0))
print()
print(obj.searchInsert2([1, 3, 5, 6], 5))
print(obj.searchInsert2([1, 3, 5, 6], 2))
print(obj.searchInsert2([1, 3, 5, 6], 7))
print(obj.searchInsert2([1, 3, 5, 6], 0))
