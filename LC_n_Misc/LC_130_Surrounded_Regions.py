class Solution:

    def dfs(self, board, r, c):
        """
        :type board: List[List[str]]
        :type r: int
        :type c: int
        :rtype: void Marking cells as visited
        """
        if r < 0 or r > len(board) - 1 or c < 0 or c > len(board[0]) - 1 or board[r][c] != 'O':
            return

        board[r][c] = 'V'
        self.dfs(board, r - 1, c)
        self.dfs(board, r + 1, c)
        self.dfs(board, r, c - 1)
        self.dfs(board, r, c + 1)

    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return

        rows, cols = len(board), len(board[0])

        for c in range(cols):
            if board[0][c] == 'O':  # chcecking first row
                self.dfs(board, 0, c)
            if board[rows - 1][c] == 'O':  # checking last row
                self.dfs(board, rows - 1, c)
        for r in range(rows):
            if board[r][0] == 'O':  # checking first column
                self.dfs(board, r, 0)
            if board[r][cols - 1] == 'O':  # checking last column
                self.dfs(board, r, cols - 1)

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'V':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'
        return