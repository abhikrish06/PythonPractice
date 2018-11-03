class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        dct = {}
        res = 0
        for ch in range(65,91):
            dct[chr(ch)] = ch - 64

        for i in range(len(s)):
            ch = s[i]
            val = dct[ch]
            # print('val: ', val)
            res = res + 26 ** (len(s)-1 - i)* val
            # print('res:', res)

        return res

obj = Solution()
print(obj.titleToNumber('ABC'))
print(obj.titleToNumber('ZZZ'))
# print(26**3 +1)
