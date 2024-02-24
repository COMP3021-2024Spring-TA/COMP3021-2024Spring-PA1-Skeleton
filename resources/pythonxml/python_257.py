class Solution:
    def dfs(self, grid, i, j):
        n = len(grid)
        m = len(grid[0])
        if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] == 0:
            return 0
        ans = 1
        grid[i][j] = 0
        ans += self.dfs(grid, i + 1, j)
        ans += self.dfs(grid, i, j + 1)
        ans += self.dfs(grid, i - 1, j)
        ans += self.dfs(grid, i, j - 1)
        return ans

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    ans = max(ans, self.dfs(grid, i, j))
        return ans