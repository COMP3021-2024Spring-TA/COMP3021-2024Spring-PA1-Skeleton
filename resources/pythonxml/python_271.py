class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        left, right = 0, 0
        ans = 0
        window_count = 0
        vowel_set = ('a','e','i','o','u')

        while right < len(s):
            if s[right] in vowel_set:
                window_count += 1

            if right - left + 1 >= k:
                ans = max(ans, window_count)
                if s[left] in vowel_set:
                    window_count -= 1
                left += 1

            right += 1
        return ans