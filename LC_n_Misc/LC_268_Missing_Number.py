class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # nums.append(len(nums))
        # for k,v in enumerate(nums):
        #     print(k,v)
        return sum(nums) - (len(nums)*(len(nums)-1))//2

obj = Solution()
print(obj.missingNumber([9,6,4,2,3,5,7,0,1]))