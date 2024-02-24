class Solution:
    
    def compress(self, chars: List[str]) -> int:
        def reverse(left, right):
            while left < right:
                chars[left], chars[right] = chars[right], chars[left]
                left += 1
                right -= 1

        slow, fast = 0, 0
        while fast < len(chars):
            fast_start = fast
            while fast + 1 < len(chars) and chars[fast + 1] == chars[fast]:
                fast += 1
            
            chars[slow] = chars[fast_start]
            slow += 1

            if fast - fast_start > 0:
                cnt = fast - fast_start + 1
                slow_start = slow
                while cnt != 0:
                    chars[slow] = str(cnt % 10)
                    slow += 1
                    cnt = cnt // 10
                reverse(slow_start, slow - 1)
            
            fast += 1
        return slow