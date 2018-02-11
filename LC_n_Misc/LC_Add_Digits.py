class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        n = len(str(num))
        # sum_n = 0
        if n == 1:
            return print(num)
        else:
            return self.addDigits(int(sum(map(int, str(num)[:]))))

obj = Solution()
obj.addDigits(12345)
obj.addDigits(38)
obj.addDigits(128)
obj.addDigits(0)
