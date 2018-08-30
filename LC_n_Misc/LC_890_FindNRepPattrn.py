class Solution:
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        res = []
        for i in range(len(words)):
            dct = {}
            val = True
            for j in range(len(pattern)):
                if pattern[j] not in dct:
                    if words[i][j] not in dct.values():
                        dct[pattern[j]] = words[i][j]
                    else:
                        val = False
                        break
                else:
                    if dct[pattern[j]] != words[i][j]:
                        val = False
                        break
            if val:
                res.append(words[i])
        return res


obj = Solution()
print(obj.findAndReplacePattern(["abc","deq","mee","aqq","dkd","ccc"],"abb"))
print(obj.findAndReplacePattern(["badc","abab","dddd","dede","yyxx"],"baba"))
