class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        d_J, d_S = {}, {}
        for i in J:
            if i in d_J:
                d_J[i] += 1
            else:
                d_J[i] = 1
        #print(d_J)
        for i in S:
            if i in d_S:
                d_S[i] += 1
            else:
                d_S[i] = 1
        #print(d_S)
        cntr = 0
        for s in d_S.keys():
            if s in d_J.keys():
                cntr += d_S[s]
        return print(cntr)

obj = Solution()
obj.numJewelsInStones("a", "AA")