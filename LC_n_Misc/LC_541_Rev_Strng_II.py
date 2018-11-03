class Solution:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if k == 1:
            return s

        res = []
        for i in range(0, len(s), 2*k):
            # print(s[i:i+k])
            # print(i)
            substr = s[i:i+k]
            substr2 = s[i+k: i+2*k]
            # print(substr2)
            res.append(substr[::-1])
            res.append(substr2)
        return ''.join(res)


obj = Solution()
# print(obj.reverseStr(s = "abcdefg", k = 2))
print(obj.reverseStr(s = "abcd", k = 3))
print(obj.reverseStr(s = 'abcdefghijk', k = 3))