class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        size = len(nums)
        if size <= 2:
            return size
        slow, fast = 2, 2
        while (fast < size):
            if nums[slow - 2] != nums[fast]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow