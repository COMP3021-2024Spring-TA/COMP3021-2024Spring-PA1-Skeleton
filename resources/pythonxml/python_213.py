class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        ans = 0
        for i in range(1, 27):
            left, right = 0, 0
            window_count = 0
            less_k_count = 0
            letter_map = dict()
            while right < len(s):
                if s[right] in letter_map:
                    letter_map[s[right]] += 1
                else:
                    letter_map[s[right]] = 1

                if letter_map[s[right]] == 1:
                    window_count += 1
                    less_k_count += 1
                if letter_map[s[right]] == k:
                    less_k_count -= 1

                while window_count > i:
                    letter_map[s[left]] -= 1
                    if letter_map[s[left]] == 0:
                        window_count -= 1
                        less_k_count -= 1
                    if letter_map[s[left]] == k - 1:
                        less_k_count += 1
                    left += 1

                if window_count == i and less_k_count == 0:
                    ans = max(right - left + 1, ans)
                right += 1
        return ans