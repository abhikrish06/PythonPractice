class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dct = {}
        for i in range(len(nums)):
            if nums[i] in dct:
                dct[nums[i]].append(i)
            else:
                dct[nums[i]] = [i]

        for v in dct.values():
            for i in range(len(v)-1,0,-1):
                if v[i] - v[i-1] <= k:
                    return True
        return False

obj = Solution()
print(obj.containsNearbyDuplicate(nums = [1,2,3,1], k = 3))
print(obj.containsNearbyDuplicate(nums = [1,0,1,1], k = 1))
print(obj.containsNearbyDuplicate(nums = [1,2,3,1,2,3], k = 2))
