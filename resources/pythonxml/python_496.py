class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        left, right = 0, 0
        window_sum = 0
        score = 0
        while right < len(calories):
            window_sum += calories[right]

            if right - left + 1 >= k:
                if window_sum < lower:
                    score -= 1
                elif window_sum > upper:
                    score += 1
                window_sum -= calories[left]
                left += 1

            right += 1
        return score