class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join(s.split()[::-1])


obj = Solution()
# print(obj.reverseWords("the sky is blue"))
print(obj.reverseWords("   a   b "))
