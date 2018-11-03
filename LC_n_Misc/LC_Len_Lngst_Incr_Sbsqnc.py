class Solution:
    def lengthOfLIS(self, nums):  # TLE :-(
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dp = [1]*len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)

    def lengthOfLIS2(self, nums):
        def search(temp, left, right, target):
            if left == right:
                return left
            mid = left + (right - left) / 2
            return search(temp, mid + 1, right, target) if temp[mid] < target else search(temp, left, mid, target)

        temp = []
        for num in nums:
            pos = search(temp, 0, len(temp), num)
            if pos >= len(temp):
                temp.append(num)
            else:
                temp[pos] = num
        return len(temp)

obj = Solution()
print(obj.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))