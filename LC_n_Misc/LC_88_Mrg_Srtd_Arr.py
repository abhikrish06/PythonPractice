class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        nums1 = nums1[:m - n + 1]
        for i in range(n):
            for j in range(m):
                if nums2[i] <= nums1[j]:
                    nums1 = nums1[:j] + [nums2[i]] + nums1[j:]
        return nums1

    def merge1(self, nums1, m, nums2, n):
        if m == 0:
            nums1 = nums2
            return nums1
        for i in range(n):
            for j in range(m):
                if nums2[i] <= nums1[j]:
                    nums1.insert(j, nums2[i])
                    nums1.pop()
                    break
        return nums1


obj = Solution()
# print(obj.merge([2, 0], 1, [1], 1))
# print(obj.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
print(obj.merge1([2, 0], 1, [1], 1))
print(obj.merge1([0], 0, [1], 1))
print(obj.merge1([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
