class Solution:
    def totalMoney(self, n: int) -> int:
        weak, day = 1, 1
        ans = 0
        for i in range(n):
            ans += weak + day - 1
            day += 1
            if day == 8:
                day = 1
                weak += 1
        
        return ans