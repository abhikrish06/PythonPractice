import math
class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # n_len = len(str(n))
        if n == 0:
            return 0

        fact_n = math.factorial(n)
        s = str(fact_n)
        # print(s)
        cntr = 0
        for i in range(len(s)-1,0,-1):
            if s[i] == '0':
                cntr += 1
            else:
                break

        return cntr

obj = Solution()
print(obj.trailingZeroes(9052))