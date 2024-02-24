class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numDict = dict()
        for num in nums:
            if num in numDict:
                numDict[num] += 1
            else:
                numDict[num] = 1
        max = float('-inf')
        max_index = -1
        for num in numDict:
            if numDict[num] > max:
                max = numDict[num]
                max_index = num
        return max_index