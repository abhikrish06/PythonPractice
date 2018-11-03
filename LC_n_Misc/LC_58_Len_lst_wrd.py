class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_trim = s.strip()

        if not s_trim:
            return 0
        lst = s_trim.split(' ')
        print(lst)
        return len(lst[-1])

# or
# x = s.split()
# return len(x[-1]) if len(x)>0 else 0


obj = Solution()
print(obj.lengthOfLastWord('a '))
print(obj.lengthOfLastWord('Hello World'))
print(obj.lengthOfLastWord(''))
print()
print(obj.lengthOfLastWord(' '))