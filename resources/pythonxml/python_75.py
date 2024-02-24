class Solution:
    def subsets(self, S):                   
        n = len(S)                          
        sub_sets = []                       
        for i in range(1 << n):             
            sub_set = []                    
            for j in range(n):              
                if i >> j & 1:              
                    sub_set.append(S[j])    
            sub_sets.append(sub_set)        
        return sub_sets                     