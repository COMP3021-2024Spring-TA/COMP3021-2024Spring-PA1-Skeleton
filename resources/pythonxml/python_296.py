class Solution:
    def numWays(self, n: int) -> int:
        if n == 0:
            return 1

        f1, f2, f3 = 0, 1, 1
        for i in range(2, n + 1):
            f1, f2 = f2, f3
            f3 = (f1 + f2) % 1000000007
        return f3