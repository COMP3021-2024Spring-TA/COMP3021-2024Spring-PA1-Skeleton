class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        if n == 0:
            return False

        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] > nums[left]:
                if nums[left] <= target and target <= nums[mid]:
                    right = mid
                else:
                    left = mid + 1
            elif nums[mid] < nums[left]:
                if nums[mid] < target and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid
            else:
                if nums[mid] == target:
                    return True
                else:
                    left = left + 1

        return nums[left] == target