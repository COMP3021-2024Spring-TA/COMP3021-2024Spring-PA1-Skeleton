class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        rows, cols = len(matrix), len(matrix[0])
        left, right = matrix[0][0], matrix[rows - 1][cols - 1] + 1
        while left < right:
            mid = left + (right - left) // 2
            if self.counterKthSmallest(mid, matrix) >= k:
                right = mid
            else:
                left = mid + 1
        return left

    def counterKthSmallest(self, mid, matrix):
        rows, cols = len(matrix), len(matrix[0])
        count = 0
        j = cols - 1
        for i in range(rows):
            while j >= 0 and mid < matrix[i][j]:
                j -= 1
            count += j + 1
        return count