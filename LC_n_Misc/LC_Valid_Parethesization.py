class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        stck = []
        if n % 2 != 0:
            return False
        match_set = set([('(',')'),('{','}'),('[', ']')])
        start = set('({[')
        for char in s:
            if char in start:
                stck.append(char)
            else:
                if len(stck) == 0:
                    return False
                lastopen = stck.pop()
                if (lastopen, char) not in match_set:
                    return False
        return len(stck) == 0

obj = Solution()
print(obj.isValid('()'))
print(obj.isValid('([)]'))