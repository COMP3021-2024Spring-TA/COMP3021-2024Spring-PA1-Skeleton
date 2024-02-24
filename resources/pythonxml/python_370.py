class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        size = len(nums)
        ans = 0

        for i in range(2, size):
            left = 0
            right = i - 1
            while left < right:
                if nums[left] + nums[right] <= nums[i]:
                    left += 1
                else:
                    ans += (right - left)
                    right -= 1
        return ans