# https://leetcode.com/contest/weekly-contest-67/problems/prime-number-of-set-bits-in-binary-representation/
import math


class Solution:
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        dict_i = {}
        cntr = 0
        for i in range(L, R + 1, 1):
            binI = bin(i).lstrip('0b')
            dict_i[i] = binI.count('1')
            # print(binI.lstrip('0b'))
        for v in dict_i.values():
            if v > 1 and self.isPrime(v):
                cntr += 1

        # print(dict_i)
        return cntr

    def isPrime(self, x):
        # print('x:', x)
        if x >= 2:
            for i in range(2, x):
                if x % i == 0:
                    return False
        else:
            return False
        return True


obj = Solution()
print(obj.countPrimeSetBits(6,10))
# print(obj.isPrime(4))
