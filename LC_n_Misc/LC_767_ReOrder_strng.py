import collections
class Solution:
    def reorganizeString(self, S):
        c = collections.Counter(S)
        if max(c.values()) <= (len(S) + 1) / 2:
            res = ""
            while c:
                out = c.most_common(2)
                print(out)
                if len(out):
                    res += out[0][0]
                    print('res: ', res)
                    c[out[0][0]] -= 1
                print('coll bef:', c)
                if len(out) > 1:
                    res += out[1][0]
                    print('res2: ', res)
                    c[out[1][0]] -= 1
                c = c + collections.Counter()
                print('coll aft: ', c)
            return res
        return ""

obj = Solution()
print(obj.reorganizeString('aba'))