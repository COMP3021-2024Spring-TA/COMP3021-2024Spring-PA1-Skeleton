class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        @cache
        def dfs(state, curTotal):
            for k in range(1, maxChoosableInteger + 1):             
                if state >> (k - 1) & 1 != 0:                       
                    continue
                if curTotal + k >= desiredTotal:                    
                    return True
                if not dfs(state | (1 << (k - 1)), curTotal + k):   
                    return True
            return False                                            

        
        if maxChoosableInteger >= desiredTotal:
            return True
            
        
        if (1 + maxChoosableInteger) * maxChoosableInteger // 2 < desiredTotal:
            return False
        return dfs(0, 0)