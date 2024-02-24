class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = float('inf')
        size = len(nums)
        for i in range(2, size):
            left = 0
            right = i - 1
            while left < right:
                total = nums[left] + nums[right] + nums[i]
                if abs(total - target) < abs(res - target):
                    res = total
                if total < target:
                    left += 1
                else:
                    right -= 1

        return res