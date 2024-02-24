class Solution:
    def canMake(self, bloomDay, days, m, k):
        count = 0
        flower = 0
        for i in range(len(bloomDay)):
            if bloomDay[i] <= days:
                flower += 1
                if flower == k:
                    count += 1
                    flower = 0
            else:
                flower = 0
        return count >= m

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m > len(bloomDay) / k:
            return -1

        left, right = min(bloomDay), max(bloomDay)

        while left < right:
            mid = left + (right - left) // 2
            if not self.canMake(bloomDay, mid, m, k):
                left = mid + 1
            else:
                right = mid

        return left