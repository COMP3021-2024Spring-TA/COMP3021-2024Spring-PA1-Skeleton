class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left, right = 0, 0
        ans = 0
        zero_count = 0

        while right < len(nums):
            if nums[right] == 0:
                zero_count += 1
            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            ans = max(ans, right - left + 1)
            right += 1

        return ans