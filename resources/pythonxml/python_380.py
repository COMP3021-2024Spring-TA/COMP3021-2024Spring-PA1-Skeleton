class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        for i in range(len(nums)):
            for j in range(len(nums) - i - 1):
                if nums[j] == 0 and nums[j + 1] != 0:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]