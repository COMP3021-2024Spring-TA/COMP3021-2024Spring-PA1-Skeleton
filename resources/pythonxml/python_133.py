class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        nums_set = set(nums)
        for num in nums_set:
            if num - 1 not in nums_set:
                curr_num = num
                curr_streak = 1
                
                while curr_num + 1 in nums_set:
                    curr_num += 1
                    curr_streak += 1
                ans = max(ans, curr_streak)

        return ans