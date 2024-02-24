class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        def get_mode(low, high):
            if low == high:
                return nums[low]
            
            mid = low + (high - low) // 2
            left_mod = get_mode(low, mid)
            right_mod = get_mode(mid + 1, high)

            if left_mod == right_mod:
                return left_mod

            left_mod_cnt, right_mod_cnt = 0, 0
            for i in range(low, high + 1):
                if nums[i] == left_mod:
                    left_mod_cnt += 1
                if nums[i] == right_mod:
                    right_mod_cnt += 1
            
            if left_mod_cnt > right_mod_cnt:
                return left_mod
            return right_mod

        return get_mode(0, len(nums) - 1)