class Solution:
    dct = {}
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        if m == 1 or n == 1:
            val = 1
        else:
            if (m,n) in self.dct:
                return self.dct[(m,n)]
            else:
                val = self.uniquePaths(m, n-1) + self.uniquePaths(m-1, n)
        self.dct[(m, n)] = val
        return val

obj = Solution()
print(obj.uniquePaths(23,12))