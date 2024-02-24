class Heapq:
    def compare(self, a, b):
        dist_a = a[0] * a[0] + a[1] * a[1]
        dist_b = b[0] * b[0] + b[1] * b[1]
        if dist_a < dist_b:
            return -1
        elif dist_a == dist_b:
            return 0
        else:
            return 1
    
    def heapAdjust(self, nums: [int], index: int, end: int):
        left = index * 2 + 1
        right = left + 1
        while left <= end:
            
            max_index = index
            if self.compare(nums[left], nums[max_index]) == -1:
                max_index = left
            if right <= end and self.compare(nums[right], nums[max_index]) == -1:
                max_index = right
            if index == max_index:
                
                break
            nums[index], nums[max_index] = nums[max_index], nums[index]
            
            index = max_index
            left = index * 2 + 1
            right = left + 1

    
    def heapify(self, nums: [int]):
        size = len(nums)
        
        for i in range((size - 2) // 2, -1, -1):
            
            self.heapAdjust(nums, i, size - 1)

    
    def heappush(self, nums: list, value):
        nums.append(value)
        size = len(nums)
        i = size - 1
        
        while (i - 1) // 2 >= 0:
            cur_root = (i - 1) // 2
            
            if self.compare(nums[cur_root], value) == -1:
                break
            
            nums[i] = nums[cur_root]
            i = cur_root
        
        nums[i] = value

    
    def heappop(self, nums: list) -> int:
        size = len(nums)
        nums[0], nums[-1] = nums[-1], nums[0]
        
        top = nums.pop()
        if size > 0:
            self.heapAdjust(nums, 0, size - 2)

        return top

    
    def heapSort(self, nums: [int]):
        self.heapify(nums)
        size = len(nums)
        for i in range(size):
            nums[0], nums[size - i - 1] = nums[size - i - 1], nums[0]
            self.heapAdjust(nums, 0, size - i - 2)
        return nums

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = Heapq()
        queue = []
        for point in points:
            heap.heappush(queue, point)

        res = []
        for i in range(k):
            res.append(heap.heappop(queue))

        return res