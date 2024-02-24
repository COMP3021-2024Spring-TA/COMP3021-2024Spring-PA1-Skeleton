class Solution:
    def pre(self, val):
        return (val + 1) >> 1

    def countOdds(self, low: int, high: int) -> int:
        return self.pre(high) - self.pre(low - 1)