class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        srt_nums = sorted(nums)
        n = len(nums)

        # if nums == srt_nums:
        #     return 0

        left, right = 0, n - 1

        while left < right:
            if nums[left] != srt_nums[left]:
                break
            left += 1

        while right > left:
            if nums[right] != srt_nums[right]:
                break
            right -= 1

        return right - left + 1 if right > left else 0

obj = Solution()
print(obj.findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]))
