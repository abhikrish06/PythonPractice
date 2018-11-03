class Solution:
    def dfs(self, grid, r, c):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == 0:
            return 0

        grid[r][c] = 0
        up = self.dfs(grid, r - 1, c)
        down = self.dfs(grid, r + 1, c)
        right = self.dfs(grid, r, c + 1)
        left = self.dfs(grid, r, c - 1)

        return up + down + left + right + 1

    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        rows, cols = len(grid), len(grid[0])
        mx_area = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    mx_area = max(mx_area, self.dfs(grid, r, c))

        return mx_area
