class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        flag_col0 = False
        flag_row0 = False
        for i in range(rows):
            if matrix[i][0] == 0:
                flag_col0 = True
                break

        for j in range(cols):
            if matrix[0][j] == 0:
                flag_row0 = True
                break

        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0

        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if flag_col0:
            for i in range(rows):
                matrix[i][0] = 0

        if flag_row0:
            for j in range(cols):
                matrix[0][j] = 0