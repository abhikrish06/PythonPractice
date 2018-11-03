class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if len(triangle) == 1:
            return triangle[0][0]

        if len(triangle) == 2:
            return min(triangle[0][0]+triangle[1][0], triangle[0][0]+triangle[1][1])

        for lvl in range(len(triangle)-2, -1, -1):
            rw = triangle[lvl]
            nxtrw = triangle[lvl+1]

            for i in range(len(rw)):
                rw[i] += min(nxtrw[i], nxtrw[i+1])
        return triangle[0][0]

obj = Solution()
print(obj.minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
print(obj.minimumTotal([[-1], [2, 3], [1, -1, -3]]))
