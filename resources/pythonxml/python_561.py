class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left, right = 0, 0
        window_count = 0
        ans = 0

        while right < len(nums):
            if nums[right] == 0:
                window_count += 1

            while window_count > 1:
                if nums[left] == 0:
                    window_count -= 1
                left += 1
            ans = max(ans, right - left + 1 - window_count)
            right += 1

        if ans == len(nums):
            return len(nums) - 1
        else:
            return ans