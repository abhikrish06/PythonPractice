class Solution:
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        S = S.replace(')(',')+(')
        print(S)
        S = S.replace('()','1')
        print(S)
        S = S.replace(')',')*2')
        print(S)

        return eval(S)

obj = Solution()
print(obj.scoreOfParentheses('(()(()))'))


# for i in range(5-1):
#     print(i)