class Solution:
    # def is_int32(self,number):
    #     try:
    #         return not (int(number) >> 32)
    #     except ValueError:
    #         return False

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = []
        if x == 0:
            return 0
        if x < 0:
            x = abs(x)
            res.append('-')

        while x > 0:
            res.append(str(x%10))
            x //= 10

        val = int(''.join(res))
        #print(val)
        if val > 2 ** 31 - 1 or val < -2**31:
            return 0
        else:
            return val




obj = Solution()
print(obj.reverse(-123354))
print(obj.reverse(123))
print(obj.reverse(-123))
print(obj.reverse(120))
print(obj.reverse(0))
print(obj.reverse(1534236469))
print(obj.reverse(-2147483648))