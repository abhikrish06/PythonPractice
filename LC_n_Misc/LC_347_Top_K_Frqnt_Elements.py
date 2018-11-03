from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        str_nums = map(str, nums)

        nums_dct = Counter(str_nums)

        sorted_lst = sorted(nums_dct.items(), key=lambda kv: kv[1], reverse=True)

        return [int(d[0]) for d in sorted_lst[:k]]


x = {'a': 2, 'b': 4, 'c': 3, 'd': 1, 'e': 0}
sorted_by_value = sorted(x.items(), key=lambda kv: kv[1], reverse=True)[:2]
print(sorted_by_value)


obj = Solution()
print(obj.topKFrequent(nums = [1,1,1,2,2,3], k = 2))
print(obj.topKFrequent(nums = [1], k = 1))
