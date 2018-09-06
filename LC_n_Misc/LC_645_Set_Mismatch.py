class Solution:
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        set_nums = set(nums)
        res.append(sum(nums) - sum(set_nums))

        ln = len(nums)

        orig_set = {i for i in range(1, ln + 1)}

        res.append((orig_set - set_nums).pop())
        # print(dct, set_nums, orig_set)

        return res

        # return [sum(nums) - sum(set(nums)), len(nums)*(len(nums)+1)//2 - sum(set(nums))]


obj = Solution()
print(obj.findErrorNums(nums=[1, 2, 2, 4]))
print(obj.findErrorNums(nums=[1, 2, 3, 3]))
