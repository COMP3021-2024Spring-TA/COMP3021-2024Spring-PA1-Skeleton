class Solution:
    
    def diagonalBinarySearch(self, matrix, diagonal, target):
        left = 0
        right = diagonal
        while left < right:
            mid = left + (right - left) // 2
            if matrix[mid][mid] < target:
                left = mid + 1
            else:
                right = mid
        return left
    
    def rowBinarySearch(self, matrix, begin, cols, target):
        left = begin
        right = cols
        while left < right:
            mid = left + (right - left) // 2
            if matrix[begin][mid] < target:
                left = mid + 1
            elif matrix[begin][mid] > target:
                right = mid - 1
            else:
                left = mid
                break
        return begin <= left <= cols and matrix[begin][left] == target

    def colBinarySearch(self, matrix, begin, rows, target):
        left = begin + 1
        right = rows
        while left < right:
            mid = left + (right - left) // 2
            if matrix[mid][begin] < target:
                left = mid + 1
            elif matrix[mid][begin] > target:
                right = mid - 1
            else:
                left = mid
                break
        return begin <= left <= rows and matrix[left][begin] == target

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        if rows == 0:
            return False
        cols = len(matrix[0])
        if cols == 0:
            return False

        min_val = min(rows, cols)
        index = self.diagonalBinarySearch(matrix, min_val - 1, target)
        if matrix[index][index] == target:
            return True
        for i in range(index + 1):
            row_search = self.rowBinarySearch(matrix, i, cols - 1, target)
            col_search = self.colBinarySearch(matrix, i, rows - 1, target)
            if row_search or col_search:
                return True
        return False