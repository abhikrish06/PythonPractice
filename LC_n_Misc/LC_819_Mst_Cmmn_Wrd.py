import re
class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        para = paragraph.lower()
        lst = para.split()
        dct, dct1 = {}, []
        for wrd in lst:
            wrd_np = re.findall(r'[a-z]+', wrd)
            #print('wrd_np: ', wrd_np)
            if wrd_np[0] in dct:
                dct[wrd_np[0]] += 1
            else:
                dct[wrd_np[0]] = 1
        #print(dct)

        dct1 = sorted(dct.keys(), key=lambda k: dct[k], reverse=True)
        for k in dct1:
            if k in banned:
                continue
            else:
                return k


obj = Solution()
print(obj.mostCommonWord('Bob hit a ball, the hit BALL flew far after it was hit.', ["hit"]))
