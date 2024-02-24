class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        f1 = 0
        f2 = 0
        f3 = 1
        for i in range(2, n + 1):
            f1, f2 = f2, f3
            f3 = (f1 + f2) % 1000000007
        return f3