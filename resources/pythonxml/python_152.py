class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        numDict = dict()
        nums = []
        for num in nums1:
            if num not in numDict:
                numDict[num] = 1
        for num in nums2:
            if num in numDict and numDict[num] != 0:
                numDict[num] -= 1
                nums.append(num)
        return nums