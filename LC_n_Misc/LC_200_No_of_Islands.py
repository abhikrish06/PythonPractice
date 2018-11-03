class Solution:
    def dfs(self, grid, r, c):

        grid[r][c] = '0'

        if r > 0 and grid[r - 1][c] == '1':
            self.dfs(grid, r - 1, c)

        if r < len(grid) - 1 and grid[r + 1][c] == '1':
            self.dfs(grid, r + 1, c)

        if c > 0 and grid[r][c - 1] == '1':
            self.dfs(grid, r, c - 1)

        if c < len(grid[0]) - 1 and grid[r][c + 1] == '1':
            self.dfs(grid, r, c + 1)

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        cnt = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    cnt += 1
                    self.dfs(grid, r, c)

        return cnt
