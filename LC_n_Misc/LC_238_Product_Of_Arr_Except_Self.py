class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # if not nums:
        #     return 0
        # res = []
        # prod = 1
        #
        # for i in range(len(nums)):
        #     res.append(prod)
        #     prod *= nums[i]
        #
        # prod = 1
        #
        # for j in range(len(nums)-1, -1, -1):
        #     res[j] *= prod
        #     prod *= nums[j]
        #
        # return res
        n = len(nums)
        res = [1]*n
        l,r = 0, n-1
        lval, rval = 1, 1

        while r > -1:
            res[l] *= lval
            res[r] *= rval
            lval *= nums[l]
            rval *= nums[r]
            l += 1
            r -= 1
            print(res)
        return res


obj = Solution()
print(obj.productExceptSelf([1,2,3,4]))
