class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        rows, cols = len(board), len(board[0])

        def dfs(x, y):
            if not 0 <= x < rows or not 0 <= y < cols or board[x][y] != 'O':
                return
            board[x][y] = '#'
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)

        for i in range(rows):
            dfs(i, 0)
            dfs(i, cols - 1)

        for j in range(cols - 1):
            dfs(0, j)
            dfs(rows - 1, j)

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == '#':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'