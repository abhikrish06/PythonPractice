class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        str_n = str(bin(n))
        bol = True
        for i in range(len(str_n)-1):
            if str_n[i] == str_n[i+1]:
                bol = False
                break
        return bol

obj = Solution()
print(obj.hasAlternatingBits(5))
print(obj.hasAlternatingBits(7))
print(obj.hasAlternatingBits(11))
print(obj.hasAlternatingBits(10))
print(5 ^ (5 >> 1))