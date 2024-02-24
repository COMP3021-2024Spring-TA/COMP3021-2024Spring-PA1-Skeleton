class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        left = max(weights)
        right = sum(weights)

        while left < right:
            mid = (left + right) >> 1
            days = 1
            cur = 0
            for weight in weights:
                if cur + weight > mid:
                    days += 1
                    cur = 0
                cur += weight

            if days <= D:
                right = mid
            else:
                left = mid + 1
        return left