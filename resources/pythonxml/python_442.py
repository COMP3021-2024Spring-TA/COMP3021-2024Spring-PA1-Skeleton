class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        bucket_dict = dict()
        for i in range(len(nums)):
            
            num = nums[i] // (t + 1)

            
            if num in bucket_dict:
                return True

            
            bucket_dict[num] = nums[i]

            
            if (num - 1) in bucket_dict and abs(bucket_dict[num - 1] - nums[i]) <= t:
                return True
            
            if (num + 1) in bucket_dict and abs(bucket_dict[num + 1] - nums[i]) <= t:
                return True
            
            if i >= k:
                bucket_dict.pop(nums[i - k] // (t + 1))

        return False