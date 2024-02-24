class Solution:
    
    def heapify(self, nums, nums_dict, index, end):
        left = index * 2 + 1
        right = left + 1
        while left <= end:
            
            max_index = index
            if nums_dict[nums[left]] > nums_dict[nums[max_index]]:
                max_index = left
            if right <= end and nums_dict[nums[right]] > nums_dict[nums[max_index]]:
                max_index = right
            if index == max_index:
                
                break
            nums[index], nums[max_index] = nums[max_index], nums[index]
            
            index = max_index
            left = index * 2 + 1
            right = left + 1

    
    def buildMaxHeap(self, nums, nums_dict):
        size = len(nums)
        
        for i in range((size - 2) // 2, -1, -1):
            self.heapify(nums, nums_dict, i, size - 1)
        return nums

    
    def maxHeapSort(self, nums, nums_dict):
        self.buildMaxHeap(nums)
        size = len(nums)
        for i in range(size):
            nums[0], nums[size - i - 1] = nums[size - i - 1], nums[0]
            self.heapify(nums, nums_dict, 0, size - i - 2)
        return nums

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        nums_dict = dict()
        for num in nums:
            if num in nums_dict:
                nums_dict[num] += 1
            else:
                nums_dict[num] = 1

        
        new_nums = list(set(nums))
        size = len(new_nums)
        
        self.buildMaxHeap(new_nums, nums_dict)
        res = list()
        for i in range(k):
            
            res.append(new_nums[0])
            
            new_nums[0], new_nums[size - i - 1] = new_nums[size - i - 1], new_nums[0]
            self.heapify(new_nums, nums_dict, 0, size - i - 2)
        return res