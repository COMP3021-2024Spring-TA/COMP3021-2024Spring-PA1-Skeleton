class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        numSet = set(nums)

        for num in range(len(nums)+1):
            if num not in numSet:
                return num