class Solution:
    directs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def dfs(self, grid, i, j):
        n, m = len(grid), len(grid[0])
        if i < 0 or i >= n or j < 0 or j >= m:
            return False
        if grid[i][j] == 1:
            return True
        grid[i][j] = 1

        res = True
        for direct in self.directs:
            new_i = i + direct[0]
            new_j = j + direct[1]
            if not self.dfs(grid, new_i, new_j):
                res = False
        return res

    def closedIsland(self, grid: List[List[int]]) -> int:
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0 and self.dfs(grid, i, j):
                    res += 1

        return res