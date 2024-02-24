class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        size = len(nums)
        res = 0
        for i in range(size):
            left, right = i + 1, size - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < target:
                    res += (right - left)
                    left += 1
                else:
                    right -= 1
        return res