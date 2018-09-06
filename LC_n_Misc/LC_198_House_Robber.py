class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev, curr = 0, 0

        for v in nums:
            prev, curr = curr, max(prev+v, curr)

        return curr