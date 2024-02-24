class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        window_size = len(cardPoints) - k
        window_sum = 0
        cards_sum = sum(cardPoints)
        min_sum = cards_sum

        left, right = 0, 0
        if window_size == 0:
            return cards_sum

        while right < len(cardPoints):
            window_sum += cardPoints[right]

            if right - left + 1 >= window_size:
                min_sum = min(window_sum, min_sum)
                window_sum -= cardPoints[left]
                left += 1

            right += 1

        return cards_sum - min_sum