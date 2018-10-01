class Solution:
    def twoSum(self, nums, target):
        if len(nums) <= 1:
            return False
        dict = {}            # defining empty dictionary
        for i in range(len(nums)):
            if nums[i] in dict:
                return [dict[nums[i]], i]
            else:
                dict[target - nums[i]] = i


obj = Solution()
print(obj.twoSum([4,4], 8))