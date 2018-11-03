class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs = sorted(strs)
        for i, ch in enumerate(strs[0]):
            for oth in strs:
                if oth[i] != ch:
                    return str[0][:i]
        return str[0]
