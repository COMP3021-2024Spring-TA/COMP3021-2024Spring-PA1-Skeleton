class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_dict = dict()
        for ch in s:
            if ch in s_dict:
                s_dict[ch] += 1
            else:
                s_dict[ch] = 1

        for ch in t:
            if ch in s_dict and s_dict[ch] != 0:
                s_dict[ch] -= 1
            else:
                return ch