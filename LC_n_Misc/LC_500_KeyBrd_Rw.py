from collections import Counter

class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        res = []
        r1, r2, r3 = 'qwertyuiop', 'asdfghjkl', 'zxcvbnm'
        # print(sorted(r1))
        for word in words:
            if set(word.lower()) <= set(r1):
                res.append(word)
            elif set(word.lower()) <= set(r2):
                res.append(word)
            elif set(word.lower()) <= set(r3):
                res.append(word)

        return res

obj = Solution()
print(obj.findWords(["Hello", "Alaska", "Dad", "Peace"]))
# print(obj.findWords(["Alaska", "Dad"]))

# wrd = 'Apple'
# print(set(wrd.lower()))