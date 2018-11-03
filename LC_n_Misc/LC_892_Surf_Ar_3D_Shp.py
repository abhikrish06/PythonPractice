class Solution:
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ar  = 0
        rows, cols = len(grid), len(grid)
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]:
                    ar += (grid[row][col])*4 + 2
                if row:
                    ar -= (min(grid[row-1][col], grid[row][col]))*2
                if col:
                    ar -= (min(grid[row][col-1], grid[row][col]))*2
        return ar


obj = Solution()
print(obj.surfaceArea([[2]]))
print(obj.surfaceArea([[1, 2], [3, 4]]))
print(obj.surfaceArea([[1, 0], [0, 2]]))
print(obj.surfaceArea([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
print(obj.surfaceArea([[2, 2, 2], [2, 1, 2], [2, 2, 2]]))
