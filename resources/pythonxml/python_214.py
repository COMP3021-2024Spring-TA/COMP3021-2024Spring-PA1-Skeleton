class Solution:
    def sortColors(self, nums: List[int]) -> None:
        left = 0
        right = len(nums) - 1
        index = 0
        while index <= right:
            if index < left:
                index += 1
            elif nums[index] == 0:
                nums[index], nums[left] = nums[left], nums[index]
                left += 1
            elif nums[index] == 2:
                nums[index], nums[right] = nums[right], nums[index]
                right -= 1
            else:
                index += 1