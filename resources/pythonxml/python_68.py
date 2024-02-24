class Solution:
    def countTriples(self, n: int) -> int:
        cnt = 0
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                c = int(sqrt(a * a + b * b + 1))
                if c <= n and a * a + b * b == c * c:
                    cnt += 1
        return cnt