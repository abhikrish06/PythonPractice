class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return str(bin(n)).count('1')

obj = Solution()
print(obj.hammingWeight(11))