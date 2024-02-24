class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        size = len(nums)

        def dfs(i, cur_sum):
            if i == size:
                if cur_sum == target:
                    return 1
                else:
                    return 0
            ans = dfs(i + 1, cur_sum - nums[i]) + dfs(i + 1, cur_sum + nums[i])
            return ans
        
        return dfs(0, 0)