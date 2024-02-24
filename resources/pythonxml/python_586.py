class Solution:
    def findMaxLength(self, nums1, nums2, i, j):
        size1, size2 = len(nums1), len(nums2)
        max_len = 0
        cur_len = 0
        while i < size1 and j < size2:
            if nums1[i] == nums2[j]:
                cur_len += 1
                max_len = max(max_len, cur_len)
            else:
                cur_len = 0
            i += 1
            j += 1
        return max_len

    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        size1, size2 = len(nums1), len(nums2)
        res = 0
        for i in range(size1):
            res = max(res, self.findMaxLength(nums1, nums2, i, 0))

        for i in range(size2):
            res = max(res, self.findMaxLength(nums1, nums2, 0, i))
        
        return res