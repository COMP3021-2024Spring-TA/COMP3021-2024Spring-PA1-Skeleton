class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numDict = dict()
        for num in nums:
            if num in numDict:
                return True
            else:
                numDict[num] = num
        return False