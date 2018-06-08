class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        bin_n = '{:032b}'.format(n)
        str_n = str(bin_n)
        rev_n = str_n[::-1]

        return int(rev_n, 2)

obj = Solution()
print(obj.reverseBits(43261596))
# print(int('00111001011110000010100101',2))