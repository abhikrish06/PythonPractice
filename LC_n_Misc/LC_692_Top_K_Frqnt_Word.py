import collections, heapq

class Solution:
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        word_dct = collections.Counter(words)
        heap = []
        for key, val in word_dct.items():
            heap.append((-val, key))

        top = heapq.nsmallest(k, heap)

        return [item[1] for item in top]

obj = Solution()
print(obj.topKFrequent(["i", "love", "leetcode", "i", "love", "coding", 'cat', 'cat'], 3))
print(obj.topKFrequent(["i", "love", "leetcode", "i", "love", "coding", "cat", "cat"], 2))
