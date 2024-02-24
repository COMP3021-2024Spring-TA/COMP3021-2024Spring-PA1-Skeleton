class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        right = 0
        window_total = 0
        ans = float('-inf')
        while right < len(nums):
            window_total += nums[right]

            if right - left + 1 >= k:
                ans = max(window_total / k, ans)
                window_total -= nums[left]
                left += 1

            
            right += 1

        return ans