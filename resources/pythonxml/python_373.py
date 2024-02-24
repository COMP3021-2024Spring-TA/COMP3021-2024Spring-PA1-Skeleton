class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 0:
            return 0
        if k % 2 == 1:
            return self.kthGrammar(n - 1, (k + 1) // 2)
        else:
            return abs(self.kthGrammar(n - 1, k // 2) - 1)