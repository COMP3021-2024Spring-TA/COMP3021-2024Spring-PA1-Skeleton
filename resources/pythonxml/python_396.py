class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        size = len(arr)
        ans = 0
        for i in range(size):
            for j in range(i + 1, size):
                temp_ans = 0
                temp_i = i
                temp_j = j
                k = j + 1
                while k < size:
                    if arr[temp_i] + arr[temp_j] == arr[k]:
                        temp_ans += 1
                        temp_i = temp_j
                        temp_j = k
                    k += 1
                if temp_ans > ans:
                    ans = temp_ans

        if ans > 0:
            return ans + 2
        else:
            return ans