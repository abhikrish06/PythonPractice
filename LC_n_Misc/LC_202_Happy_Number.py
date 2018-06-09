class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s = set()

        while n != 1:
            if n in s:
                return False
            s.add(n)
            n = sum(map(lambda x: x**2, map(int, list(str(n)))))
        return True

obj = Solution()
print(obj.isHappy(91))
print(obj.isHappy(10))