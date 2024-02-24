class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        stack = []
        size = len(height)
        for i in range(size):
            while stack and height[i] > height[stack[-1]]:
                cur = stack.pop(-1)
                if stack:
                    left = stack[-1] + 1
                    right = i - 1
                    high = min(height[i], height[stack[-1]]) - height[cur]
                    ans += high * (right - left + 1)
                else:
                    break
            stack.append(i)
        return ans