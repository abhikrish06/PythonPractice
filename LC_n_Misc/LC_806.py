# from collections import Counter

class Solution:
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        res = []
        s_dict = {}
        str_all_dict = {}
        tot_len = 0
        str_all = 'abcdefghijklmnopqrstuvwxyz'
        for c, v in enumerate(str_all):
            str_all_dict[v] = c

        for ch in S:
            if ch in s_dict:
                s_dict[ch][0] += 1
            else:
                s_dict[ch] = [1, str_all_dict[ch]]

        for k, v in s_dict.items():
            tot_len = tot_len + v[0] * widths[v[1]]

        if tot_len % 100 == 0:
            res.append(tot_len // 100)
            res.append(0)
        else:
            res.append((tot_len // 100) + 1)
            res.append(widths[s_dict[S[-1]][1]])

        return res

obj = Solution()
print(obj.numberOfLines([4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], "bbbcccdddaaa"))
