class Solution:
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """

        if not S:
            return ['']

        res = [S, S.upper()]

        for ch in S:
            s1 = S[:]
            if ch in 'abcdefghijklmnopqrstuvwxyz':
                s1 = S.replace(ch, ch.upper(), 1)
                res.append(s1)

        return res

obj = Solution()
print(obj.letterCasePermutation("aa1b2"))
