class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        left = 0
        right = 0
        window_count = 0
        ans = 0

        while right < len(customers):
            if grumpy[right] == 1:
                window_count += customers[right]

            if right - left + 1 > minutes:
                if grumpy[left] == 1:
                    window_count -= customers[left]
                left += 1

            right += 1
            ans = max(ans, window_count)

        for i in range(len(customers)):
            if grumpy[i] == 0:
                ans += customers[i]
        return ans