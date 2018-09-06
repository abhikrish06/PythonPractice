class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        return num ^ (1<< len(bin(num))-2)-1

obj = Solution()
print(obj.findComplement(5))