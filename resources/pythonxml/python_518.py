class Solution:
    def bubbleSort(self, nums: [int]) -> [int]:
        
        for i in range(len(nums) - 1):
            flag = False    
            
            for j in range(len(nums) - i - 1):
                
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    flag = True
            if not flag:    
                break
        
        return nums
    
    def sortArray(self, nums: [int]) -> [int]:
        return self.bubbleSort(nums)