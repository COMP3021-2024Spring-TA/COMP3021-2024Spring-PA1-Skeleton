class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)                       
        sub_sets = []                       
        for i in range(1 << n):             
            sub_set = []                    
            for j in range(n):              
                if i >> j & 1:              
                    sub_set.append(nums[j]) 
            sub_sets.append(sub_set)        
        return sub_sets                     