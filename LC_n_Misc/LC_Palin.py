class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return print(list(str(x)) == list(str(x)[::-1]))

obj = Solution()
obj.isPalindrome(121)
obj.isPalindrome(123)