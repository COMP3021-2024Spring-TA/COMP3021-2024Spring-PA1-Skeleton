class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        window_sum = 0
        left, right = 0, 0
        window = dict()
        ans = 0
        while right < len(nums):
            window_sum += nums[right]
            if nums[right] not in window:
                window[nums[right]] = 1
            else:
                window[nums[right]] += 1

            while window[nums[right]] > 1:
                window[nums[left]] -= 1
                window_sum -= nums[left]
                left += 1
            ans = max(ans, window_sum)
            right += 1
        return ans