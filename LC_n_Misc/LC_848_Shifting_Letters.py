class Solution:
    def shiftingLetters(self, S, shifts):
        """
        :type S: str
        :type shifts: List[int]
        :rtype: str
        """
        for i in range(len(shifts) - 2, -1, -1):
            shifts[i] += shifts[i + 1]
        res = ''
        for c,s in zip(S, shifts):
            res = res + "".join(chr((ord(c) - 97 + s) % 26 + 97))
        return res

obj = Solution()
print(obj.shiftingLetters(S="abc", shifts=[3, 5, 9]))

# print(677%26)
