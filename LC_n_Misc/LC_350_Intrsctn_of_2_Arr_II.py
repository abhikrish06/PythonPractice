from collections import Counter

class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        nums1_dct = Counter(nums1)

        for k in nums2:
            if k in nums1_dct.keys() and nums1_dct[k] > 0:
                res.append(k)
                nums1_dct[k] -= 1
        return res

        # one liner
        # return list((Counter(nums1) & Counter(nums2)).elements())

obj = Solution()
print(obj.intersect(nums1 = [1,2,2,1], nums2 = [2,2]))
print(obj.intersect(nums1 = [4,9,5], nums2 = [9,4,9,8,4]))

# nums1 = [4,9,5]
# nums2 = [9,4,9,8,4]
