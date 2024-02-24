class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        size = len(nums)

        for i in range(size):
            while 1 <= nums[i] <= size and nums[i] != nums[nums[i] - 1]:
                index1 = i
                index2 = nums[i] - 1
                nums[index1], nums[index2] = nums[index2], nums[index1]

        for i in range(size):
            if nums[i] != i + 1:
                return i + 1
        return size + 1