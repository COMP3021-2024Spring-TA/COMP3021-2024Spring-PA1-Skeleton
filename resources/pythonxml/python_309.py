class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        size = len(arr)
        ans = 0
        idx_map = dict()
        for idx, value in enumerate(arr):
            idx_map[value] = idx
        
        for i in range(size):
            for j in range(i + 1, size):
                temp_ans = 0
                temp_i = i
                temp_j = j
                while arr[temp_i] + arr[temp_j] in idx_map:
                    temp_ans += 1
                    k = idx_map[arr[temp_i] + arr[temp_j]]
                    temp_i = temp_j
                    temp_j = k

                if temp_ans > ans:
                    ans = temp_ans

        if ans > 0:
            return ans + 2
        else:
            return ans