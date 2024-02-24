left = 0
right = 0

while right < len(nums):
    window.append(nums[right])
    
    while 窗口需要缩小:
        
        window.popleft()
        left += 1
    
    
    right += 1