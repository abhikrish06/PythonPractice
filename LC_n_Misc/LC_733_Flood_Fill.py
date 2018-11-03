class Solution:
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """

        row, col, colr = len(image), len(image[0]), image[sr][sc]

        def dfs(i, j):
            if (not (0 <= i < row and 0 <= j < col)) or image[i][j] != colr:
                return
            image[i][j] = newColor
            [dfs(i+x, j+y) for (x,y) in ((0, 1), (1, 0), (0, -1), (-1, 0))]

        if colr != newColor:
            dfs(sr, sc)

        return image

obj = Solution()
print(obj.floodFill(image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, newColor = 2))