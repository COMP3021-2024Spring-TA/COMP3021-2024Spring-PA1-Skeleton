class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = 0
        for j in range(len(nums)):
            sum = 0
            for i in range(j, -1, -1):
                sum += nums[i]
                if sum == k:
                    cnt += 1
        
        return cnt