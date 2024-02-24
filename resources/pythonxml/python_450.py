class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums_dict = dict()
        for num in nums:
            if num in nums_dict:
                nums_dict[num] += 1
            else:
                nums_dict[num] = 1
        for key in nums_dict:
            value = nums_dict[key]
            if value == 1:
                return key
        return 0