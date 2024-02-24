class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        size = len(nums)
        left, right = 0, size - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left