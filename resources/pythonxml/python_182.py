class Solution:
    def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
        """
        Do not return anything, modify A in-place instead.
        """
        arr = []
        index_A, index_B = 0, 0
        while index_A < m and index_B < n:
            if A[index_A] <= B[index_B]:
                arr.append(A[index_A])
                index_A += 1
            else:
                arr.append(B[index_B])
                index_B += 1
        while index_A < m:
            arr.append(A[index_A])
            index_A += 1
        while index_B < n:
            arr.append(B[index_B])
            index_B += 1
        for i in range(m + n):
            A[i] = arr[i]