# from collections import OrderedDict
# class Solution:
#     def countOfAtoms(self, formula):
#         """
#         :type formula: str
#         :rtype: str
#         """
#         dct = OrderedDict()
#         self.add2Dct(formula, dct)
#         return dct
#
#     def add2Dct(self, formula, dct):
#         n = len(formula)
#         i = 0
#         while i < n - 2:
#             if formula[i].isupper():
#                 if formula[i + 1].islower():
#                     strT = formula[i] + formula[i + 1]
#                     if formula[i + 2].isdigit():
#                         if strT in dct:
#                             dct[strT] += int(formula[i + 2])
#                             i += 3
#                         else:
#                             dct[strT] = int(formula[i + 2])
#                             i += 3
#                     # elif formula[i + 2].isdigit():
#                     #     if strT in dct:
#                     #         dct[strT] += 1
#                     #         i += 2
#                     #     else:
#                     #         dct[strT] = 1
#                     #         i += 2
#                 elif formula[i + 1].isdigit():
#                     if formula[i] in dct:
#                         dct[formula[i]] += int(formula[i + 1])
#                         i += 1
#                     else:
#                         dct[formula[i]] = int(formula[i + 1])
#                         i += 1
#                 else:
#                     if formula[i] in dct:
#                         dct[formula[i]] += 1
#                         i += 1
#                     else:
#                         dct[formula[i]] = 1
#                         i += 1
#             elif formula[i] == '(':
#                 cnt = 1
#                 str2 = '('
#                 i += 1
#                 while cnt >= 0:
#                     if formula[i] == '(':
#                         cnt += 1
#                         str2 = str2 + formula[i]
#                         i += 1
#                     elif formula[i] == ')':
#                         cnt -= 1
#                         str2 = str2 + formula[i]
#                         i += 1
#                     else:
#                         str2 = str2 + formula[i]
#                         i += 1
#                 self.add2Dct(str2[1:-1], dct)
#                 n1 = len(str2)
#                 i += n1
#         return None

from collections import Counter
class Solution:
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        stk = [Counter()]
        n = len(formula)
        i = 0
        while i < n:
            if formula[i] == '(':
                stk.append(Counter())
                i += 1
            elif formula[i] == ')':
                top = stk.pop()
                i += 1
                newI = i
                while i < n and formula[i].isdigit(): i += 1
                mul = int(formula[newI:i] or 1)
                for k,v in top.items():
                    stk[-1][k] += v*mul
            else:
                newI = i
                i += 1

                while i < n and formula[i].islower(): i += 1
                k = formula[newI:i]

                newI = i
                while i < n and formula[i].isdigit(): i += 1
                mul = int(formula[newI:i] or 1)
                stk[-1][k] += mul

        res = ''

        for k in sorted(stk[-1]):
            if stk[-1][k] > 1:
                res = res + k + str(stk[-1][k])
            else:
                res = res + k
        return res

obj = Solution()
print(obj.countOfAtoms('H2O'))

