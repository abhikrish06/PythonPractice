from collections import Counter

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ''
        dct = Counter(s)
        sorted_dct_val = sorted(dct.items(), key=lambda kv:kv[1], reverse=True)
        for tpl in sorted_dct_val:
            res += (tpl[0])* tpl[1]
        return res

obj = Solution()
print(obj.frequencySort('Aabb'))
print(obj.frequencySort('cccaaa'))
print(obj.frequencySort('tree'))