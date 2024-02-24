class Solution:
    def minOperations(self, n: int) -> int:
        ans = 0
        for i in range(n // 2):
            ans += n - 1 - 2 * i
        return ans