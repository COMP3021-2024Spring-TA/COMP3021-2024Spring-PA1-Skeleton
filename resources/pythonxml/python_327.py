class Solution:
    def canEat(self, piles, hour, speed):
        time = 0
        for pile in piles:
            time += (pile + speed - 1) // speed
        return time <= hour

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        while left < right:
            mid = left + (right - left) // 2
            if not self.canEat(piles, h, mid):
                left = mid + 1
            else:
                right = mid

        return left