from collections import Counter

class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        nums_dict = dict(Counter(nums))
        print(nums_dict)
        for i in range(1, len(nums)+1):
            if i in nums_dict.keys():
                continue
            else:
                res.append(i)
        return res

obj = Solution()
print(obj.findDisappearedNumbers([4,3,2,7,8,2,3,1]))