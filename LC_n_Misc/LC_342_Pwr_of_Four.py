class Solution:
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        str_bin = str(bin(num))[2:]

        ones = str_bin.count('1')
        zeros = str_bin.count('0')

        print(bin(num), str_bin, ones, zeros)

        if ones == 1:
            if zeros % 2 == 0:
                return True

        return False
    # one liner:
    # return num > 0 and bin(num).count('1') ==  1 and bin(num).count('0') % 2 == 1

obj = Solution()
print(obj.isPowerOfFour(-64))