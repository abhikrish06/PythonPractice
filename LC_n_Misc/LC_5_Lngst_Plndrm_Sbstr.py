# TLE
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2 or s == s[::-1]:
            return s

        max_len_sbstr = ''

        for i in range(len(s)):
            for j in range(i, len(s), 1):
                sbstr = s[i:j + 1]
                print('sbstr:', sbstr)
                if sbstr == sbstr[::-1]:
                    if len(sbstr) > len(max_len_sbstr):
                        max_len_sbstr = sbstr
        return max_len_sbstr

obj = Solution()
print(obj.longestPalindrome("abb"))