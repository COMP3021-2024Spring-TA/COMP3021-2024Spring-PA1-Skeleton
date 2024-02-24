class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        nums_dict = dict()
        for num in nums:
            if num in nums_dict:
                return num
            nums_dict[num] = 1
        return -1