class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # d n c

        if not nums or len(nums) < 4:
            return []

        nums.sort()

        return [list(t) for t in self.kSum(nums, target, 4)]

    def kSum(self, nums, target, k):
        """
        :type nums = List[int]
        :type target: int
        :type k: int
        :rtype: List[int]
        """
        res = set()
        if k == 2:
            lo, hi = 0, len(nums) - 1

            while lo < hi:
                if nums[lo] + nums[hi] == target:
                    res.add((nums[lo], nums[hi]))
                    lo += 1
                elif nums[lo] + nums[hi] < target:
                    lo += 1
                else:
                    hi -= 1

        else:
            lo = 0

            while lo < len(nums) - k + 1:
                for n in self.kSum(nums[lo + 1:], target - nums[lo], k - 1):
                    res.add((nums[lo],) + tuple(n))
                lo += 1

        return res