class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        size1, size2 = len(nums1), len(nums2)
        ans = 0
        for i in range(size1):
            for j in range(size2):
                if nums1[i] == nums2[j]:
                    subLen = 1
                    while i + subLen < size1 and j + subLen < size2 and nums1[i + subLen] == nums2[j + subLen]:
                        subLen += 1
                    ans = max(ans, subLen)
        
        return ans