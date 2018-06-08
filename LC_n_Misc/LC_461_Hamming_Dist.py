class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        val = bin(x ^ y)
        return val.count('1')


obj = Solution()
print(obj.hammingDistance(2,4))