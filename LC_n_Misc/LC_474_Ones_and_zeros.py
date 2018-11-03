class Solution:
    def chk_max(self, strs, m, n, cur_pt):
        curr_max = 0
        for i in range(cur_pt,len(strs)):
            zeros, ones = strs[i].count('0') ,strs[i].count('1')
            if m >= zeros and n >= ones:
                curr_max = max(curr_max, self.chk_max(strs, m-zeros, n-ones, i+1)+1)
        return curr_max

    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        return self.chk_max(strs, m, n, 0)

obj = Solution()
obj.findMaxForm(["10", "0001", "111001", "1", "0"], 5, 3)