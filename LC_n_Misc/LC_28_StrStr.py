class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not haystack and not needle:
            return 0
        elif not haystack:
            return -1
        elif not needle:
            return 0

        h, n = len(haystack), len(needle)

        for i in range(h):
            if haystack[i] == needle[0]:
                substr = haystack[i:i + n]
                #print(substr)
                if substr == needle:
                    return i
        return -1

    # more elegant soln
    def strStr2(self, haystack, needle):
        if not haystack and not needle:
            return 0
        if not needle:
            return 0
        if not haystack or not needle or len(haystack.split(needle)) == 1:
            return -1

        return len(haystack.split(needle)[0])


obj = Solution()
print(obj.strStr("hello", "ll"))
print(obj.strStr("aaaaa", "bba"))

print(obj.strStr2("hello", "ll"))
print(obj.strStr2("aaaaa", "bba"))
