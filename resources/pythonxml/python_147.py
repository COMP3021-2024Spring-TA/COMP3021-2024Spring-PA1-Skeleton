class Solution:
    directs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def dfs(self, grid, i, j):
        rows = len(grid)
        cols = len(grid[0])
        if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == 0:
            return
        grid[i][j] = 0

        for direct in self.directs:
            new_i = i + direct[0]
            new_j = j + direct[1]
            self.dfs(grid, new_i, new_j)

    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            if grid[i][0] == 1:
                self.dfs(grid, i, 0)
            if grid[i][cols - 1] == 1:
                self.dfs(grid, i, cols - 1)

        for j in range(cols):
            if grid[0][j] == 1:
                self.dfs(grid, 0, j)
            if grid[rows - 1][j] == 1:
                self.dfs(grid, rows - 1, j)

        ans = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    ans += 1
        return ans