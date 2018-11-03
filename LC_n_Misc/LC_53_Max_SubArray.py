class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res, curr_sum = 0, 0
        res_lst = []
        n = len(nums)
        if n == 1:
            return nums[0]
        else:
            for i in range(n):
                res = nums[i]
                for j in range(i + 1, n - 1):
                    if nums[i] < nums[j]:
                        curr_sum = sum(nums[i:j])
                    if curr_sum < res:
                        break
                    else:
                        res = curr_sum
                        res_lst.append(res)
        return max(res_lst)


obj = Solution()
print(obj.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
