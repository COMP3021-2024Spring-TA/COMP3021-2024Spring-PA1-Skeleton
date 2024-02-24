left = 0
right = 0

while right < len(nums):
    window.append(nums[right])
    
    
    if right - left + 1 >= window_size:
        
        window.popleft()
        left += 1
    
    
    right += 1