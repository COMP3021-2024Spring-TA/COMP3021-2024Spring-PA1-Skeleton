class Solution:
    def sumXor(self, x):
        if x % 4 == 0:
            return x
        if x % 4 == 1:
            return 1
        if x % 4 == 2:
            return x + 1
        return 0
    def xorOperation(self, n: int, start: int) -> int:
        s = start >> 1
        e = n & start & 1
        ans = self.sumXor(s-1) ^ self.sumXor(s + n - 1)
        return ans << 1 | e