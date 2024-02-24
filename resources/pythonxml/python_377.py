class Solution:
    def dfs(self, cur, n, res):
        if cur > n:
            return
        res.append(cur)
        for i in range(10):
            num = 10 * cur + i
            if num > n:
                return
            self.dfs(num, n, res)

    def lexicalOrder(self, n: int) -> List[int]:
        res = []
        for i in range(1, 10):
            self.dfs(i, n, res)
        return res