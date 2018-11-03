class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        dct = {}
        res = []
        for ch in range(65, 91):
            dct[ch - 65] = chr(ch)
        # dct[0] = 'Z'
        # print(dct)
        while n > 0:
            n -= 1
            ch = dct[n % 26]
            res.insert(0, ch)
            n = (n // 26)

        return ''.join(res)


obj = Solution()
print(obj.convertToTitle(1))
print(obj.convertToTitle(28))
print(obj.convertToTitle(701))
print(obj.convertToTitle(728))
print(obj.convertToTitle(18278))
# 17587