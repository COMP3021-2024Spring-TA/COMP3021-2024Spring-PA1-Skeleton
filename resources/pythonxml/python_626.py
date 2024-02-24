class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        ans = 0
        for i in range(1, math.gcd(a, b) + 1):
            if a % i == 0 and b % i == 0:
                ans += 1
        return ans