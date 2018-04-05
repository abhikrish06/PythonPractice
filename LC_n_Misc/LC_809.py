from collections import Counter, OrderedDict


class Solution:
    def expressiveWords(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        if len(words) == 0:
            return 0

        res = 0
        dct = dict(Counter(S))

        for wrd in words:
            print(wrd)
            intr = 0
            wrd_dct = dict(Counter(wrd))
            # print(dct.keys(), wrd_dct.keys())
            if wrd_dct.keys() == dct.keys():
                # print("True")
                print(dct)
                print(wrd_dct)
                for k, v in wrd_dct.items():
                    print(k, wrd_dct[k], dct[k])
                    if wrd_dct[k] == dct[k] or wrd_dct[k] >= 3:
                        intr += 1
                    else:
                        intr = 0
                        break
                print("intr", intr)
                if intr > 0:
                    res += 1
                    print("res: ", res)
        return res

obj = Solution()
print(obj.expressiveWords("heeellooo", ["hello", "hi", "helo"]))
