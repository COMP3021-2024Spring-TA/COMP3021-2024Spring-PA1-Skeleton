class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        ans = 0
        for cost in costs:
            if coins >= cost:
                ans += 1
                coins -= cost
        return ans