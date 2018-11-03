# incomplete
# TLE
class Solution:
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 0
        while i < len(s)-1:
            sub = s[:i + 1]
            print(sub)
            if s.count(sub)*len(sub) == len(s):
                return True
            else:
                i += 1
        return False

obj = Solution()
print(obj.repeatedSubstringPattern('abba'))