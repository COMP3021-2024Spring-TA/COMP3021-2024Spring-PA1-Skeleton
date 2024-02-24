class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_count = 0
        zero_count = 0
        left, right = 0, 0
        while right < len(nums):
            if nums[right] == 0:
                zero_count += 1
            right += 1
            if zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            max_count = max(max_count, right - left)
        return max_count