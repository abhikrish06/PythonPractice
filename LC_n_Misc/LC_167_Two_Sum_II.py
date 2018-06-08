class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(numbers) <= 1:
            return []
        dct = {}
        for i in range(len(numbers)):
            if numbers[i] in dct:
                return [dct[numbers[i]]+1, i+1]
            else:
                dct[target - numbers[i]] = i


obj = Solution()
print(obj.twoSum([2, 7, 11, 15], 9))
