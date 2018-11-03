# incomplete
# incorrect
class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        cntr, divdn, divdr = 0, dividend, divisor
        if dividend < 0:
            dividend = -1 * dividend
        if divisor < 0:
            divisor = -1 * divisor
        while dividend >= divisor:
            dividend = dividend - divisor
            cntr += 1
        return -1 * cntr if (divdn < 0 or divdr < 0) and not (divdn < 0 and divdr < 0) else cntr


obj = Solution()
print(obj.divide(10, 3))
print(obj.divide(7, -3))
print(obj.divide(-1, -1))
