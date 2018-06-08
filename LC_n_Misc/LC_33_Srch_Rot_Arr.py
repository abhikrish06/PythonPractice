class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lo = 0
        ri = len(nums) - 1

        while (lo <= ri):
            mid = (lo + ri) // 2
            # case 1:
            if nums[mid] == target:
                return mid

            # case  2: (sorted right)
            if nums[mid] <= nums[ri]:
                if target > nums[mid] and target <= nums[ri]:
                    lo = mid + 1
                else:
                    ri = mid - 1

            # case 3: (sorted left)
            if nums[mid] >= nums[lo]:
                if target >= nums[lo] and target < nums[mid]:
                    ri = mid - 1
                else:
                    lo = mid + 1
        return -1

obj = Solution()
print(obj.search([4, 5, 6, 7, 0, 1, 2], 3))
print(obj.search([4, 5, 6, 7, 0, 1, 2], 0))
