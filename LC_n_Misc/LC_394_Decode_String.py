import re

class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        while '[' in s:
        # patt = re.findall(r'[0-9]\[[a-z]*\]*[a-z]*', s)
            s = re.sub(r'(\d+)\[([a-zA-Z]*)\]',lambda a : int(a.group(1))* a.group(2), s)

        # print(patt)

        return s

obj = Solution()
print(obj.decodeString("3[a]2[bc]"))
print(obj.decodeString("3[a2[c]]"))
print(obj.decodeString("2[abc]3[cd]ef"))
