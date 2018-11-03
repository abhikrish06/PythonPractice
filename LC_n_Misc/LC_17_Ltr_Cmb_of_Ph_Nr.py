from itertools import product


class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        digit_dct = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'],
                     '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}

        if len(digits) == 1:
            return digit_dct[digits[0]]

        n = len(digits)
        res = ['']

        for digit in digits:
            tmp = res[:]
            tmp2 = []
            for ch in digit_dct[digit]:
                for a in tmp:
                    tmp2.append(a+ch)
                    # print(tmp2)
                res = tmp2

        return res

obj = Solution()
# print(obj.letterCombinations('23'))
print(obj.letterCombinations('234'))
