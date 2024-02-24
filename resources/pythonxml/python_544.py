class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)                       
        sub_sets = []                       
        for i in range(1 << n):             
            sub_set = []                    
            flag = True                     
            for j in range(n):  
                if i >> j & 1:  
                    if j > 0 and (i >> (j - 1) & 1) == 0 and nums[j] == nums[j - 1]:
                        flag = False        
                        break
                    sub_set.append(nums[j]) 
            if flag:
                sub_sets.append(sub_set)    
        return sub_sets                     