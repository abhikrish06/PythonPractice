# https://leetcode.com/contest/weekly-contest-67/problems/partition-labels/
from collections import OrderedDict

class Solution:
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        if not S:
            return []

        m = OrderedDict()

        for cntr, val in enumerate(S):
            if val not in m:
                m[val] = [-1, -1]
            if m[val][0] == -1:
                m[val][0] = cntr
                m[val][1] = cntr
            else:
                m[val][1] = cntr

        # print(m)

        fin_lst = []
        start, end = 0, 0
        for k, v in m.items():
            st,ed = v
            print(st, ed)
            if st > end:
                fin_lst.append(st - start)
                start = st
                end = ed
            else:
                end = max(end, ed)
            print(fin_lst)
        fin_lst.append(end-start+1)

        return fin_lst

obj = Solution()
print(obj.partitionLabels('ababcbacadefegdehijhklij'))