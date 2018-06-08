# incomplete
class Solution:
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        mp = '0123456789abcdef'
        res = []
        if num == 0:
            return 0

        return ''.join(res)


obj = Solution()
print(obj.toHex(26))
print(obj.toHex(-1))