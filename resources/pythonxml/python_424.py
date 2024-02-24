class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        zero_cnt, one_cnt = 0, 0
        res = 0
        rows, cols = len(grid), len(grid[0])

        for col in range(cols):
            for row in range(rows):
                if col == 0 and grid[row][col] == 0:
                    for j in range(cols):
                        grid[row][j] = 1 - grid[row][j]
                else:
                    if grid[row][col] == 1:
                        one_cnt += 1
                    else:
                        zero_cnt += 1
            if zero_cnt > one_cnt:
                for row in range(rows):
                    grid[row][col] = 1 - grid[row][col]

            for row in range(rows):
                if grid[row][col] == 1:
                    res += pow(2, cols - col - 1)
            zero_cnt = 0
            one_cnt = 0
        return res