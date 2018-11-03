class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        lst = s.split()
        res = []
        for wrd in lst:
            res.append(wrd[::-1])

        return " ".join(res)


obj = Solution()
print(obj.reverseWords("Let's take LeetCode contest"))