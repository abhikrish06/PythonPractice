# TLE
# class Solution(object):
#     def longestPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
#         if len(s) < 2 or s == s[::-1]:
#             return s
#
#         max_len_sbstr = ''
#
#         for i in range(len(s)):
#             for j in range(i, len(s), 1):
#                 sbstr = s[i:j + 1]
#                 print('sbstr:', sbstr)
#                 if sbstr == sbstr[::-1]:
#                     if len(sbstr) > len(max_len_sbstr):
#                         max_len_sbstr = sbstr
#         return max_len_sbstr
#
# obj = Solution()
# print(obj.longestPalindrome("abb"))
#

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        res = ""

        for i in range(len(s)):

            tmp = self.helper(s, i, i)
            if len(tmp) > len(res):
                res = tmp

            tmp = self.helper(s, i, i + 1)
            if len(tmp) > len(res):
                res = tmp

        return res

    def helper(self, s, l, r):

        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1:r]

obj = Solution()
print(obj.longestPalindrome("ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg"))


