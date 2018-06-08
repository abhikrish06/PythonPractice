class Solution:
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        cntr = 0
        for i in range(len(grid)):

        for i in range(len(grid) - 2):
            for j in range(len(grid) - 2):
                if grid[i][j] < 1 or grid[i][j] > 9:
                    break
                s1 = sum(grid[i][j:j+3])
                s2 = sum(grid[i+1][j:j+3])
                s3 = sum(grid[i+2][j:j+3])
                d1 = grid[i][j]+grid[i+1][j+1]+grid[i+2][j+2]
                d2 = grid[i][j+2]+grid[i+1][j+1]+grid[i+2][j]

                if s1 == s2 == s3 == d1 == d2:
                    cntr += 1

        return cntr


obj =Solution()
# print(obj.numMagicSquaresInside([[4,3,8,4],[9,5,1,9],[2,7,6,2]]))
print(obj.numMagicSquaresInside([[7,0,5],[2,4,6],[3,8,1]]))