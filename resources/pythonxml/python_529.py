class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1, -1]
        n = len(nums)
        if n == 0:
            return ans

        left = 0
        right = n - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid

        if nums[left] != target:
            return ans

        ans[0] = left

        left = 0
        right = n - 1
        while left < right:
            mid = left + (right - left + 1) // 2
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid

        if nums[left] == target:
            ans[1] = left

        return ans