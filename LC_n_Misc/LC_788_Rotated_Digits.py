class Solution:
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        cntr = 0
        if N == 1:
            return 0
        else:
            for i in range(1, N + 1):
                n_str = str(i)
                if '3' in n_str or '4' in n_str or '7' in n_str:
                    continue
                elif '2' in n_str or '5' in n_str or '6' in n_str or '9' in n_str:
                    cntr += 1
        return cntr


obj = Solution()
print(obj.rotatedDigits(10))
