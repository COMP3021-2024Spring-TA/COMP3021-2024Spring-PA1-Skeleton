class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if mid == nums[mid]:
                left = mid + 1
            else:
                right = mid
        if left == nums[left]:
            return left + 1
        else:
            return left