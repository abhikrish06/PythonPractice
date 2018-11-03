# incomplete

class Solution:
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 4 or sum(nums) % 4 != 0 or max(nums) > sum(nums) / 4:
            return False
        side_len = sum(nums)//4






obj = Solution()
# print(obj.makesquare([1,1,2,2,2]))
# print(obj.makesquare([3,3,3,3,4]))
print(obj.makesquare([16, 8, 8, 8, 5, 1, 16, 3, 11, 1, 11, 12, 20, 6, 6]))
