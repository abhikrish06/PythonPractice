# slow solution
# class Solution:
#     def letterCasePermutation(self, S):
#         """
#         :type S: str
#         :rtype: List[str]
#         """
#
#         if not S:
#             return ['']
#
#         s1 = S.lower()
#         res = [s1]
#
#         for i in range(len(S)-1, -1, -1):
#             n = len(res)
#             for j in range(n):
#                 if res[j][i] in 'abcdefghijklmnopqrstuvwxyz':
#                     res.append(self.rep_at_index(res[j], res[j][i], i))
#         return res
#
#     def rep_at_index(self,strng, ch, idx=0):
#         """
#         :type strng: str
#         :type ch: str
#         :type idx: int
#         :rtype: str
#         """
#         return '%s%s%s'%(strng[:idx],ch.upper(),strng[idx+1:])

class Solution:
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """

        out = [""]
        S = S.lower()
        for c in S:
            if c.isalpha():
                out = [i + j for i in out for j in [c.upper(), c.lower()]]
            else:
                out = [i + c for i in out]

        return out

obj = Solution()
print(obj.letterCasePermutation("aa1b2"))
print(obj.letterCasePermutation("abde"))
print(obj.letterCasePermutation("a1b2"))
print(obj.letterCasePermutation("3z4"))
print(obj.letterCasePermutation("12345"))
print(obj.letterCasePermutation("RmR"))
