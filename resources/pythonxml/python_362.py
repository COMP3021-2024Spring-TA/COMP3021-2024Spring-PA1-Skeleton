class Heapq:
    
    def heapAdjust(self, nums: [int], nums_dict, index: int, end: int):
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
    
    
    def heapify(self, nums: [int], nums_dict):
        size = len(nums)
        
        for i in range((size - 2) // 2, -1, -1):
            
            self.heapAdjust(nums, nums_dict, i, size - 1)
    
    
    def heappush(self, nums: list, nums_dict, value):
        nums.append(value)
        size = len(nums)
        i = size - 1
        
        while (i - 1) // 2 >= 0:
            cur_root = (i - 1) // 2
            
            if nums_dict[nums[cur_root]] > nums_dict[value]:
                break
            
            nums[i] = nums[cur_root]
            i = cur_root
        
        nums[i] = value
                
    
    def heappop(self, nums: list, nums_dict) -> int:
        size = len(nums)
        nums[0], nums[-1] = nums[-1], nums[0]
        
        top = nums.pop()
        if size > 0:
            self.heapAdjust(nums, nums_dict, 0, size - 2)
            
        return top

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        nums_dict = dict()
        for num in nums:
            if num in nums_dict:
                nums_dict[num] += 1
            else:
                nums_dict[num] = 1

        
        new_nums = list(set(nums))
        size = len(new_nums)

        heap = Heapq()
        queue = []
        for num in new_nums:
            heap.heappush(queue, nums_dict, num)
        
        res = []
        for i in range(k):
            res.append(heap.heappop(queue, nums_dict))
        return res