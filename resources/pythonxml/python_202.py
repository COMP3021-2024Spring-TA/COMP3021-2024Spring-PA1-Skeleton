class Solution:
    def searchLeft(self, nums, target):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        if nums[left] == target:
            return left
        else:
            return -1

    def searchRight(self, nums, target):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left + 1) // 2
            if nums[mid] <= target:
                left = mid
            else:
                right = mid - 1
        return left

    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return 0
        left = self.searchLeft(nums, target)
        right = self.searchRight(nums, target)

        if left == -1:
            return 0

        return right - left + 1