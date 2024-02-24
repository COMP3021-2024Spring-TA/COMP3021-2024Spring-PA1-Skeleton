class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        need = collections.defaultdict(int)
        for ch in p:
            need[ch] += 1

        window = collections.defaultdict(int)
        window_size = len(p)
        res = []
        left, right = 0, 0
        valid = 0
        while right < len(s):
            if s[right] in need:
                window[s[right]] += 1
                if window[s[right]] == need[s[right]]:
                    valid += 1

            if right - left + 1 >= window_size:
                if valid == len(need):
                    res.append(left)
                if s[left] in need:
                    if window[s[left]] == need[s[left]]:
                        valid -= 1
                    window[s[left]] -= 1
                left += 1
            right += 1
        return res