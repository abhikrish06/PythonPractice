# incomplete

# class Solution:
#     def findMedianSortedArrays(self, nums1, nums2):
#         """
#         :type nums1: List[int]
#         :type nums2: List[int]
#         :rtype: float
#         """
#         from heapq import merge
#
#         if not nums1 and not nums2:
#             return 0.0
#
#         mrg_lst = list(merge(nums1, nums2))
#         # print(mrg_lst)
#         l = len(mrg_lst)
#
#         return float(mrg_lst[l//2]) if l % 2 !=0 else (mrg_lst[(l//2)-1] +  mrg_lst[(l//2)])/2




obj = Solution()
print(obj.findMedianSortedArrays([1, 3], [2]))
print(obj.findMedianSortedArrays([1, 2], [3, 4]))
print(obj.findMedianSortedArrays([1, 2, 5, 7], [-1, 3, 4, 6, 9]))
