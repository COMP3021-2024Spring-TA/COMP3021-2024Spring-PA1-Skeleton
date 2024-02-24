class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        size_m = len(matrix)
        if size_m == 0:
            return []
        size_n = len(matrix[0])
        if size_n == 0:
            return []

        up, down, left, right = 0, size_m - 1, 0, size_n - 1
        ans = []
        while True:
            for i in range(left, right + 1):
                ans.append(matrix[up][i])
            up += 1
            if up > down:
                break
            for i in range(up, down + 1):
                ans.append(matrix[i][right])
            right -= 1
            if right < left:
                break
            for i in range(right, left - 1, -1):
                ans.append(matrix[down][i])
            down -= 1
            if down < up:
                break
            for i in range(down, up - 1, -1):
                ans.append(matrix[i][left])
            left += 1
            if left > right:
                break
        return ans