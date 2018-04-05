from collections import Counter
class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        counter_p = Counter(p)
        #print(counter_p)
        counter_s = Counter(s[:len(p)-1])
        res = []
        for i in range(len(p)-1, len(s)):
            counter_s[s[i]] += 1
            if counter_p == counter_s:
                res.append(i - len(p) + 1)
            counter_s[s[i - len(p) + 1]] -= 1
            if counter_s[s[i - len(p) + 1]] == 0:
                del counter_s[s[i - len(p) + 1]]
        return res


obj = Solution()
print(obj.findAnagrams("cbaebabacd", "abc"))