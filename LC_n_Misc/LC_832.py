class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        res, fin = [], []
        for arr in A:
            res.append(arr[::-1])
            # print(res)

        for ar in res:
            res2 = []
            for i in ar:
                if i == 0:
                    res2.append(1)
                elif i == 1:
                    res2.append(0)
            fin.append(res2)
        return fin

obj = Solution()
print(obj.flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]))
print(obj.flipAndInvertImage([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]))