class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(size, subset, index):
            res.append(subset)
            for i in range(index, size):
                backtrack(size, subset + [nums[i]], i + 1)

        size = len(nums)
        res = list()
        backtrack(size, [], 0)
        return res