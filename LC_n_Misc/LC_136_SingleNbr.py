class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for num in nums:
            res ^= num
            print("res:", res)
        return res

obj = Solution()
print(obj.singleNumber([1,2,5,2,1,4,4]))