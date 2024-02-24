class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow = 0
        fast = 0
        while fast < len(nums):
            if nums[fast] != val:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
            fast += 1
        return slow